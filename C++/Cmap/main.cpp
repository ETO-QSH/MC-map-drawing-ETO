#include <set>
#include <regex>
#include <vector>
#include <fstream>
#include <cstdlib>
#include <cstring>
#include <opencv2/opencv.hpp>
#include "allhpp/type.hpp"
#include "allhpp/KDTree.hpp"
#include "allhpp/CIEDE2000.hpp"
#include "allhpp/RGB_to_XYZ.hpp"
#include "allhpp/XYZ_to_Lab.hpp"

// 将cv::Vec3b类型的RGB颜色转换为std::vector<double>类型的LAB颜色
std::vector<double> rgb_to_lab(const cv::Vec3b& rgb_color) {

    // 将cv::Vec3b类型的RGB颜色转换为colorutil::RGB类型
    colorutil::RGB srgb_color;
    srgb_color(0) = rgb_color[0] / 255.0;
    srgb_color(1) = rgb_color[1] / 255.0;
    srgb_color(2) = rgb_color[2] / 255.0;

    // 转换为CIEXYZ
    colorutil::XYZ xyz_color = colorutil::convert_RGB_to_XYZ(srgb_color);

    // 转换为CIELAB
    colorutil::Lab lab_color = colorutil::convert_XYZ_to_Lab(xyz_color);

    // 将colorutil::Lab类型转换为std::vector<double>
    auto L = static_cast<float>(lab_color[0]);
    auto a = static_cast<float>(lab_color[1]);
    auto b = static_cast<float>(lab_color[2]);

    std::vector<double> lab_vector = {L, a, b};

    return lab_vector;
}

// 自定义比较函数
struct ColorCompare {
    bool operator()(const cv::Vec3b& a, const cv::Vec3b& b) const {
        return a[0] < b[0] || (a[0] == b[0] && a[1] < b[1]) || (a[0] == b[0] && a[1] == b[1] && a[2] < b[2]);
     }
};

int main(int argc, char** argv) {
    // 检查命令行参数数量
    if (argc != 9) {
        std::cerr << "Usage: " << argv[0] << " -i <input_image_path> -o <output_image_path> -l <colorList_path> -n <number_of_nearest_colors>" << std::endl;
        return -1;
    }

    // 解析命令行参数
    std::string colorList_path;
    std::string input_image_path;
    std::string output_image_path;
    int number_of_nearest_colors = 16;

    for (int i = 1; i < argc; ++i) {
        if (strcmp(argv[i], "-i") == 0) {
            input_image_path = argv[++i];
        } else if (strcmp(argv[i], "-o") == 0) {
            output_image_path = argv[++i];
        } else if (strcmp(argv[i], "-l") == 0) {
            colorList_path = argv[++i];
        } else if (strcmp(argv[i], "-n") == 0) {
            char* end;
            number_of_nearest_colors = static_cast<int>(strtol(argv[++i], &end, 10));
            if (*end != '\0') {
                std::cerr << "Error: Invalid number of nearest colors specified." << std::endl;
                return -1;
            }
        }
    }

     // 读取图片
     cv::Mat img = cv::imread(input_image_path, cv::IMREAD_COLOR);
     if (img.empty()) {
         std::cerr << "Error: Image not found." << std::endl;
         return -1;
     }

     // 创建一个set来存储唯一颜色值
     std::set<cv::Vec3b, ColorCompare> unique_colors;

     // 遍历图片中的每个像素
     for (int y = 0; y < img.rows; ++y) {
         for (int x = 0; x < img.cols; ++x) {
             // 获取当前像素的RGB值
             cv::Vec3b rgb_color = img.at<cv::Vec3b>(y, x);
             // 插入到set中，自动去重
             unique_colors.insert(cv::Vec3b(rgb_color[2], rgb_color[1], rgb_color[0]));
         }
     }

    // 从文本文件中读取颜色值
    std::ifstream file(colorList_path);
    std::vector<cv::Vec3b> rgb_colors;
    std::string line;
    std::getline(file, line); // 读取整行数据

    // 移除首尾的花括号
    if (line.front() == '[' && line.back() == ']') {
        line = line.substr(1, line.size() - 2); // 移除首尾的花括号
    }

    // 使用正则表达式匹配十六进制颜色值
    std::regex re("\\s*#([0-9A-Fa-f]{2})([0-9A-Fa-f]{2})([0-9A-Fa-f]{2})\\s*");
    std::smatch matches;
    std::string::const_iterator searchStart(line.cbegin());

    while (std::regex_search(searchStart, line.cend(), matches, re)) {
        if (matches.size() == 4) { // 匹配到的组数应该为4（包括整个匹配）
            int r = std::stoi(matches[1].str(), nullptr, 16);
            int g = std::stoi(matches[2].str(), nullptr, 16);
            int b = std::stoi(matches[3].str(), nullptr, 16);
            rgb_colors.emplace_back(static_cast<uchar>(r), static_cast<uchar>(g), static_cast<uchar>(b));
        }
        searchStart = matches.suffix().first;
    }
    file.close();

     // 创建一个vector来存储LAB颜色
     std::vector<std::vector<double>> lab_colors;
     lab_colors.reserve(rgb_colors.size());

     // 将RGB颜色列表转换为LAB颜色空间
     for (const auto& color : rgb_colors) {
         std::vector<double> lab = rgb_to_lab(color);
         lab_colors.push_back(lab);
     }

     // 创建KD树
     KDTree lab_tree(lab_colors);

    // 遍历所有唯一颜色
    for (const auto& color : unique_colors) {
        // 将查询的RGB颜色转换为LAB颜色空间
        std::vector<double> query_lab = rgb_to_lab(color);

        // 使用KD树找到最近的16个颜色
        pointIndexArr nearest_colors = lab_tree.nearest_pointIndices(query_lab, number_of_nearest_colors);

        // 初始化最小感知距离和对应颜色
        double min_difference = std::numeric_limits<double>::max();
        cv::Vec3b nearest_color;

        // 遍历最近的16个颜色
        for (const auto& nearest_color_index : nearest_colors) {
            // 获取最近颜色的RGB值
            cv::Vec3b nearest_color_rgb = rgb_colors[nearest_color_index.second];
            // 将RGB颜色转换为LAB颜色空间
            std::vector<double> lab_color_2 = rgb_to_lab(nearest_color_rgb);
            // 数据类型转换
            colorutil::Lab lab_color_0(query_lab[0], query_lab[1], query_lab[2]);
            colorutil::Lab lab_color_1(lab_color_2[0], lab_color_2[1], lab_color_2[2]);

            // 计算与被替换颜色的感知距离
            double difference = colorutil::calculate_CIEDE2000(lab_color_0, lab_color_1);
            // 如果当前颜色的感知距离更小，则更新最小感知距离和对应颜色
            if (difference < min_difference) {
                min_difference = difference;
                nearest_color = nearest_color_rgb;
            }
        }

        // 用找到的最近颜色替换原图的像素
        for (int y = 0; y < img.rows; ++y) {
            for (int x = 0; x < img.cols; ++x) {
                cv::Vec3b current_pixel = img.at<cv::Vec3b>(y, x);
                if (current_pixel[0] == 0 && current_pixel[1] == 0 && current_pixel[2] == 0) {
                } else {
                    if (img.at<cv::Vec3b>(y, x) == cv::Vec3b(color[2], color[1], color[0])) {
                        img.at<cv::Vec3b>(y, x) = cv::Vec3b(nearest_color[2], nearest_color[1], nearest_color[0]);
                    }
                }
            }
        }
    }

    cv::Mat rgba_image(img.rows, img.cols, CV_8UC4);

    // 将全黑像素转换为透明
    for (int y = 0; y < rgba_image.rows; ++y) {
        for (int x = 0; x < rgba_image.cols; ++x) {
            cv::Vec3b current_pixel = img.at<cv::Vec3b>(y, x);
            if (current_pixel[0] == 0 && current_pixel[1] == 0 && current_pixel[2] == 0) {
                rgba_image.at<cv::Vec4b>(y, x) = cv::Vec4b(0, 0, 0, 0);
            } else {
                rgba_image.at<cv::Vec4b>(y, x) = cv::Vec4b(current_pixel[0], current_pixel[1], current_pixel[2], 255);
            }
        }
    }

     // 保存结果
    cv::imwrite(output_image_path, rgba_image);

    return 0;
}
