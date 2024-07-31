#include <opencv2/opencv.hpp>
#include <iostream>
#include <string>
#include <sstream>

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
}

int main(int argc, char** argv) {
  // 检查命令行参数数量
  if (argc != 9) {
    std::cerr << "Usage: " << argv[0] << " -i <input_image_path> -o <output_image_path> -m <mode> -s <scale>" << std::endl;
    return -1;
  }

  // 解析命令行参数
  bool mode = true;
  std::string input_image_path;
  std::string output_image_path;
  double scale = 1.0;

  for (int i = 1; i < argc; ++i) {
    if (strcmp(argv[i], "-m") == 0) {
      std::string flag = argv[++i];
      if (flag == "true") {
        mode = true;
      }
      else if (flag == "false") {
        mode = false;
      }
      else {
        std::cerr << "Error: no " << flag << " true or false" << std::endl;
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

  // 读取图片
  cv::Mat src = cv::imread(input_image_path);
  if (src.empty()) {
    std::cout << "Could not open or find the image" << std::endl;
    return -1;
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

  // 将原图转换为BGRA格式
  cv::Mat bgraImage;
  cv::cvtColor(scaledImage, bgraImage, cv::COLOR_BGR2BGRA);

  // 计算原图在新图像中的位置
  int x = (newWidth - scaledWidth) / 2;
  int y = (newHeight - scaledHeight) / 2;

  // 将带有alpha通道的原图复制到新图像的中心位置
  bgraImage.copyTo(newImage(cv::Rect(x, y, scaledWidth, scaledHeight)));

  // 根据布尔变量的值决定是保存新图像还是分割保存
  if (mode) {
    // 保存新图像
    cv::imwrite(output_image_path, newImage);
  } else {
    // 调用函数，以"new"作为文件名前缀
    splitAndSave(newImage, output_image_path);
  }

  return 0;
}