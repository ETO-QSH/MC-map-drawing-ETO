#include <opencv2/opencv.hpp>
#include <iostream>
#include <string>
#include <sstream>
#include <windows.h>
#include <vector>
#include <algorithm>

// 旋转图片
cv::Mat rotateImage(const cv::Mat &src, int angle) {
  // 根据角度选择旋转方法
  int rotateCode = 0;
  switch (angle) {
    case 90:
      rotateCode = cv::ROTATE_90_CLOCKWISE;
    break;
    case 180:
      rotateCode = cv::ROTATE_180;
    break;
    case 270:
    case -90:
        rotateCode = cv::ROTATE_90_COUNTERCLOCKWISE;
    break;
    default:
      throw std::invalid_argument("Unsupported angle. Only 90, 180, and 270 degrees are supported.");
  }

  // 创建一个空的输出图像
  cv::Mat rotated;
  // 旋转图像
  cv::rotate(src, rotated, rotateCode);

  return rotated;
}

// 用于从文件名中提取坐标
bool extractCoordinates(const std::string& filename, int& x, int& y) {
    size_t pos1 = filename.find('_');
    size_t pos2 = filename.rfind('.');

    if (pos1 != std::string::npos && pos2 != std::string::npos && pos2 > pos1) {
        std::string coords = filename.substr(pos1 + 1, pos2 - pos1 - 1);
        // 修改格式字符串以匹配下划线分隔的整数
        if (sscanf(coords.c_str(), "%d_%d", &x, &y) == 2) {
          // 如果输入失败，返回false
          return true;
        }
    }
    // 如果没有找到下划线或点，返回false
    return false;
}

void jigsaw(const std::string& dic_path, const std::string& output_image_path) {
    WIN32_FIND_DATA findFileData;
    HANDLE hFind = FindFirstFile((dic_path + "\\*").c_str(), &findFileData);

    if (hFind == INVALID_HANDLE_VALUE) {
        std::cerr << "Error finding first file: " << GetLastError() << std::endl;
        return;
    }

    std::vector<cv::Mat> images;
    std::vector<std::pair<int, int>> coordinates;

    do {
        std::string filename = findFileData.cFileName;
        if (filename.size() > 4 && filename.substr(filename.size() - 4) == ".png") {
            int x, y;
            if (extractCoordinates(filename, x, y)) {
                std::string filepath = dic_path + "\\" + filename;
                cv::Mat img = cv::imread(filepath, cv::IMREAD_UNCHANGED);
                if (!img.empty()) {
                    images.push_back(img);
                    coordinates.emplace_back(x, y);
                }
            }
        }
    } while (FindNextFile(hFind, &findFileData) != 0);

    FindClose(hFind);

    // 按坐标排序图片
    std::sort(coordinates.begin(), coordinates.end(), [](const std::pair<int, int>& a, const std::pair<int, int>& b) {
        return a.second < b.second || (a.second == b.second && a.first < b.first);
    });

    // 初始化最大坐标值
    int maxX = 0, maxY = 0;

    // 遍历排序后的坐标，计算最大坐标值
    for (const auto& coord : coordinates) {
      int x = coord.first;
      int y = coord.second;
      maxX = std::max(maxX, x);
      maxY = std::max(maxY, y);
    }

    cv::Mat finalImage(maxY * 128, maxX * 128, CV_8UC4, cv::Scalar(0, 0, 0, 0));

    // 将每张图片放置到最终图片中
    for (size_t i = 0; i < images.size(); ++i) {
      int x = coordinates[i].first;
      int y = coordinates[i].second;
      // 确保图片放置位置在最终图像的边界内
      int xPlacement = (x-1) * 128;
      int yPlacement = (y-1) * 128;
      cv::Rect placement(xPlacement, yPlacement, images[i].cols, images[i].rows);
      images[i].copyTo(finalImage(placement));
    }

    // 保存最终图片
    cv::imwrite(output_image_path, finalImage);
}

void splitAndSave(const cv::Mat &image, const std::string &prefix) {
  // 遍历图像的每个128x128块
  for (int y = 0; y < image.rows; y += 128) {
    for (int x = 0; x < image.cols; x += 128) {
      // 提取当前块
      cv::Rect blockRect(x, y, 128, 128);
      cv::Mat block = image(blockRect);

      // 构建文件名
      std::stringstream filename;
      filename << prefix << "_" << (y / 128 + 1) << "_" << (x / 128 + 1) << ".png";

      // 保存块
      cv::imwrite(filename.str(), block);
    }
  }
  std::cout << "(" << (image.rows / 128 + 1) << "," << (image.cols / 128 + 1) << ")" << std::endl;
}

int main(int argc, char** argv) {
  // 检查命令行参数数量
  if (argc != 9) {
    std::cerr << "Usage: " << argv[0] << " -i <input_image_path> -o <output_image_path> -m <mode> -s <scale>" << std::endl;
    return -1;
  }

  // 解析命令行参数
  int mode = 0;
  std::string input_image_path;
  std::string output_image_path;
  double scale = 1.0;

  for (int i = 1; i < argc; ++i) {
    if (strcmp(argv[i], "-m") == 0) {
      std::string flag = argv[++i];
      if (flag == "none") {
        mode = -1;
      }
      else if (flag == "false") {
        mode = 0;
      }
      else if (flag == "true") {
        mode = 1;
      }
      else if (flag == "1pi") {
        mode = 90;
      }
      else if (flag == "2pi") {
        mode = 180;
      }
      else if (flag == "3pi") {
        mode = 270;
      }
      else {
        std::cerr << "Error mode: " << flag << " ((true or false) or none) or 1pi 2pi 3pi " << std::endl;
      }
    } else if (strcmp(argv[i], "-i") == 0) {
      input_image_path = argv[++i];
    } else if (strcmp(argv[i], "-o") == 0) {
      output_image_path = argv[++i];
    } else if (strcmp(argv[i], "-s") == 0) {
      char* end;
      scale = strtod(argv[++i], &end);
      if (*end != '\0') {
        std::cerr << "Error: Invalid number of nearest colors specified." << std::endl;
        return -1;
      }
    }
  }

  if (mode == -1) {

    jigsaw(input_image_path, output_image_path);

  } else if(mode == 90 or mode == 180 or mode == 270) {

    cv::Mat image = cv::imread(input_image_path, cv::IMREAD_UNCHANGED);
    cv::Mat rotatedImage = rotateImage(image, mode);
    cv::imwrite(output_image_path, rotatedImage);

  } else {

    cv::Mat src = cv::imread(input_image_path, cv::IMREAD_UNCHANGED);
    if (src.empty()) {
      std::cout << "Could not open or find the image" << std::endl;
      return -1;
    }

    // 检查图像是否已经是四通道的
    if (src.channels() == 4) {

    } else if (src.channels() == 3) {

      // 分离图像的BGR通道
      std::vector<cv::Mat> rgb3Channels;
      cv::split(src, rgb3Channels);

      // 创建一个与原图同样大小的全白Alpha通道
      cv::Mat alphaChannel(src.size(), CV_8UC1, cv::Scalar(255));

      // 将BGR通道和Alpha通道合并为一个四通道图像
      std::vector<cv::Mat> channels_4;
      channels_4.push_back(rgb3Channels[0]); // B通道
      channels_4.push_back(rgb3Channels[1]); // G通道
      channels_4.push_back(rgb3Channels[2]); // R通道
      channels_4.push_back(alphaChannel);    // Alpha通道

      cv::Mat img_alpha_0;
      cv::merge(channels_4, img_alpha_0);

      // 将合并后的四通道图像赋值回src
      src = img_alpha_0;
    }

    // 获取原图尺寸
    int srcWidth = src.cols;
    int srcHeight = src.rows;

    // 计算缩放后的尺寸
    int scaledWidth = static_cast<int>(srcWidth * scale);
    int scaledHeight = static_cast<int>(srcHeight * scale);

    // 保持纵横比不变，进行四舍五入
    if (scaledWidth % 2 != 0) scaledWidth++;
    if (scaledHeight % 2 != 0) scaledHeight++;

    // 创建缩放后的过渡图像
    cv::Mat scaledImage;
    cv::resize(src, scaledImage, cv::Size(scaledWidth, scaledHeight), 0, 0, cv::INTER_LINEAR);

    // 计算新图像的尺寸
    int newWidth = ((scaledWidth + 127) / 128) * 128;
    int newHeight = ((scaledHeight + 127) / 128) * 128;

    // 创建一个新的图像，类型为CV_8UC4，即8位无符号4通道图像（BGR + Alpha）
    cv::Mat newImage(newHeight, newWidth, CV_8UC4, cv::Scalar(0, 0, 0, 0));

    // 计算原图在新图像中的位置
    int x = (newWidth - scaledWidth) / 2;
    int y = (newHeight - scaledHeight) / 2;

    // 将带有alpha通道的原图复制到新图像的中心位置
    scaledImage.copyTo(newImage(cv::Rect(x, y, scaledWidth, scaledHeight)));

    // 根据布尔变量的值决定是保存新图像还是分割保存
    if (mode == 1) {
      // 保存新图像
      cv::imwrite(output_image_path, newImage);
    } else {
      // 调用函数，以"Label"作为文件名前缀
      splitAndSave(newImage, output_image_path);
    }
  }

  return 0;
}