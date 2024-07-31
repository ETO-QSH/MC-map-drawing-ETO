#include <opencv2/opencv.hpp>
#include "json.hpp"
#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <map>

// 定义枚举类型来表示f的三种状态
enum class FState { None, True, False };

// 全局变量
int upon = 0, down = 0;

// longest函数的C++版本
std::pair<int, int> longest(const std::vector<int>& lst) {
    int turn = -1;
    int first_length = 0;
    int max_length_two = 0;
    int max_length_zero = 0;
    int current_length_two = 0;
    int current_length_zero = 0;

    for (int i : lst) {
        if (i == 0) {
            current_length_zero += 1;
            max_length_zero = std::max(max_length_zero, current_length_zero);
            current_length_two = 0;
            if (turn == -1 || turn == 0) {
                first_length -= 1;
                turn = 0;
            } else {
                turn = 1;
            }
        } else if (i == 2) {
            current_length_two += 1;
            max_length_two = std::max(max_length_two, current_length_two);
            current_length_zero = 0;
            if (turn == -1 || turn == 2) {
                first_length += 1;
                turn = 2;
            } else {
                turn = 1;
            }
        }
    }

    return std::make_pair(first_length, std::max(max_length_zero, max_length_two) + 1);
}

// hlist函数的C++版本
std::vector<int> hlist(const std::vector<int>& lst, const std::pair<int, int>& ags) {
    int first_length = ags.first;
    int max_length = ags.second;
    int first = first_length > 0 ? first_length : -first_length;
    FState f = FState::True;
    std::vector<int> new_lst;
    int h = 0, j = 0, u = 0, d = 0, Hmode = 0;
    if (max_length == first + 1) {
        if (lst[0] == 1) {
            u = 0, d = 0;
        } else if (lst[0] == 0) {
            u = 0, d = first_length;
        } else if (lst[0] == 2) {
            d = 0, u = first_length;
        }
    }
    for (int i : lst) {
        if (f == FState::True) {
            if (i == 1) {
                h = 0;
            } else {
                if (i == 0) {
                    h = -1;
                } else if (i == 2) {
                    h = 1;
                }
                first -= 1;
                f = FState::False;
            }
            new_lst.push_back(h);
        } else if (first > 0) {
            if (i == 0) {
                h -= 1;
                first -= 1;
            } else if (i == 2) {
                h += 1;
                first -= 1;
            }
            new_lst.push_back(h);
        } else {
            if (f == FState::False) {
                if (h < 0) {
                    d = h;
                    u = h + max_length - 1;
                } else if (h > 0) {
                    u = h;
                    d = h - max_length + 1;
                }
                f = FState::None;
            }
            if (i == 1) {
                j += 1;
                new_lst.push_back(h);
            } else if (i == 0) {
                if (Hmode == 2) {
                    h = d;
                    j = 1;
                } else if (Hmode == 0) {
                    h = d;
                    j += 1;
                    for (int k = 1; k < j; ++k) {
                        new_lst[new_lst.size() - k] += 1;
                    }
                }
                new_lst.push_back(h);
            } else if (i == 2) {
                if (Hmode == 0) {
                    h = u;
                    j = 1;
                } else if (Hmode == 2) {
                    h = u;
                    j += 1;
                    for (int k = 1; k < j; ++k) {
                        new_lst[new_lst.size() - k] -= 1;
                    }
                }
                new_lst.push_back(h);
            }
            if (i != 1) {
                Hmode = i;
            }
        }
        if (u > upon) {
            upon = u;
        }
        if (d < down) {
            down = d;
        }
    }
    return new_lst;
}

int main(int argc, char** argv) {
    // 检查命令行参数数量
    if (argc != 11) {
        std::cerr << "Usage: " << argv[0] << " -i <png_path> -c <colorList> -p <pixivColor> -k <key_value_list_txt> -n <mode>" << std::endl;
        return -1;
    }

    // 解析命令行参数
    std::string key_value_list_txt;
    std::string pixivColor;
    std::string colorList;
    std::string png_path;
    int mode = 3;

    for (int i = 1; i < argc; ++i) {
        if (strcmp(argv[i], "-i") == 0) {
            png_path = argv[++i];
        } else if (strcmp(argv[i], "-c") == 0) {
            colorList = argv[++i];
        } else if (strcmp(argv[i], "-p") == 0) {
            pixivColor = argv[++i];
        } else if (strcmp(argv[i], "-k") == 0) {
            key_value_list_txt = argv[++i];
        } else if (strcmp(argv[i], "-n") == 0) {
            char* end;
            mode = static_cast<int>(strtol(argv[++i], &end, 10));
            if (*end != '\0') {
                std::cerr << "Error!" << std::endl;
                return -1;
            }
        }
    }

    // 读取图片
    cv::Mat img = cv::imread(png_path, cv::IMREAD_COLOR);
    if (img.empty()) {
        std::cerr << "Error: Image not found." << png_path << std::endl;
        return -1;
    }

    // 从文本文件中读取颜色值
    std::ifstream file(colorList);
    std::map<std::string, int> color_index_map;
    std::string line;
    std::getline(file, line);

    // 移除首尾的花括号
    if (line.front() == '[' && line.back() == ']') {
        line = line.substr(1, line.size() - 2);
    }

    // 使用正则表达式匹配十六进制颜色值
    std::regex re("\\s*#([0-9A-Fa-f]{2})([0-9A-Fa-f]{2})([0-9A-Fa-f]{2})\\s*");
    std::smatch matches;
    std::string::const_iterator searchStart(line.cbegin());

    int index = 0;
    while (std::regex_search(searchStart, line.cend(), matches, re)) {
        if (matches.size() == 4) {
            std::string color_str = "#" + matches[1].str() + matches[2].str() + matches[3].str();
            color_index_map[color_str] = index++;
        }
        searchStart = matches.suffix().first;
    }
    file.close();

    // 创建一个新的二维列表来存储转换后的字典列表
    std::vector<std::vector<std::map<std::string, std::string>>> transformed_list;

    // 创建一个新的二维列表来存储转换后的字典的值
    std::vector<std::vector<int>> transformed_values_list;

    // 创建一个字符串用于存储所有转换后的十六进制数值
    std::string hex_values;

    // 遍历图片中的每个像素
    for (int y = 0; y < img.rows; ++y) {
        std::vector<std::map<std::string, std::string>> row_list;
        std::vector<int> row_values_list;
        for (int x = 0; x < img.cols; ++x) {
            // 获取当前像素的RGB值
            cv::Vec3b RGB_color = img.at<cv::Vec3b>(y, x);
            // 将颜色转换为字符串形式
            std::ostringstream oss;
            oss << "#";
            oss << std::hex << std::setw(2) << std::setfill('0') << std::uppercase << static_cast<int>(RGB_color[2])
                << std::hex << std::setw(2) << std::setfill('0') << std::uppercase << static_cast<int>(RGB_color[1])
                << std::hex << std::setw(2) << std::setfill('0') << std::uppercase << static_cast<int>(RGB_color[0]);
            std::string color_str = oss.str();

            // 查找颜色在color_index_map中的索引
            auto it = color_index_map.find(color_str);
            if (it != color_index_map.end()) {
                // 计算键和值
                std::string key = "0";
                std::string value = "1";

                if (it->second != 0) {
                    key = std::to_string(((it->second - 1) / 4) + 1);
                    value = std::to_string((it->second - 1) % 4);
                } else {
                    key = std::to_string(0);
                    value = std::to_string(1);
                }

                // 创建字典并添加到当前行的列表中
                std::map<std::string, std::string> color_dict = {{key, value}};
                row_list.push_back(color_dict);

                // 将字典的值添加到当前行的值列表中
                std::string dict_value = color_dict.begin()->second;
                int dict_value_int = std::stoi(dict_value);
                row_values_list.push_back(dict_value_int);

                // 将索引偏移后的十六进制数值添加到字符串中
                int index_plus = 1;
                if (it->second != 0) {
                    index_plus = it->second + 4 - 1;
                } else {
                    index_plus = 1;
                }

                std::ostringstream hex_stream;
                hex_stream << std::hex << std::uppercase << "0x" << std::setw(2) << std::setfill('0') << index_plus;
                std::string hex_value = hex_stream.str();
                hex_values += hex_value + ", ";
            } else {
                // 如果颜色不在color_index_map中，可以添加一个默认值或进行其他处理
                std::map<std::string, std::string> color_dict = {{"0", "1"}};
                row_list.push_back(color_dict);
            }
        }
        // 将当前行的列表添加到新的二维列表中
        transformed_list.push_back(row_list);

        // 将当前行的值列表添加到新的二维列表中
        transformed_values_list.push_back(row_values_list);
    }

    // 移除最后一个多余的逗号和空格
    if (!hex_values.empty()) {
        hex_values.pop_back();
        hex_values.pop_back();
    }

    try {
        // 没意义，屡试不爽
        throw "ETO";
    }

    catch (...) {
        // 打开文件用于写入，如果文件不存在则创建它
        std::ofstream ofile(pixivColor);
        if (!ofile.is_open()) {
            std::cerr << "无法打开文件" << std::endl;
            return 1;
        }
        ofile << hex_values;
        ofile.close();

        if (mode == 3 or mode == 1) {
            // 创建一个新列表 lst，用于存储行列置换后的二维列表
            std::vector<std::vector<int>> lst;
            for (size_t col = 0; col < transformed_values_list[0].size(); ++col) {
                std::vector<int> new_row;
                for (auto & row : transformed_values_list) {
                    new_row.push_back(row[col]);
                }
                lst.push_back(new_row);
            }

            // 创建一个新的二维列表来存储键值对
            std::vector<std::vector<std::pair<std::string, int>>> key_value_list;

            // 遍历transformed_list二维列表
            for (int row = 0; row < transformed_list.size(); ++row) {
                std::vector<std::pair<std::string, int>> key_value_row;
                std::vector<int> new_lst = hlist(lst[row], longest(lst[row]));
                for (int col = 0; col < transformed_list[row].size(); ++col) {
                    // 遍历字典中的每个键值对--将[col][row]颠倒一下
                    for (const auto& pair : transformed_list[col][row]) {
                        // 获取new_lst中相同坐标的元素作为值
                        int zvalue = 0;
                        if (mode==3) {
                            zvalue = new_lst[col];
                        } else if (mode==1) {
                            zvalue = 0;
                        } else if (mode==4) {
                            zvalue = -1;
                        }
                        // 将键和值转换为字典形式并添加到当前行的列表中
                        std::pair<std::string, int> key_value_str = {pair.first, zvalue};
                        key_value_row.push_back(key_value_str);
                    }
                }
                // 将当前行的列表添加到新的二维列表中
                key_value_list.push_back(key_value_row);
            }

            // 创建一个JSON对象
            nlohmann::json json_obj;

            json_obj["u-d"] = nlohmann::json::array({upon, down});
            json_obj["blocks"] = nlohmann::json::array();

            for (size_t i = 0; i < key_value_list.size(); ++i) {
                // 为每个中间层创建一个空数组
                json_obj["blocks"].push_back(nlohmann::json::array());
                for (size_t j = 0; j < key_value_list[i].size(); ++j) {
                    // 获取键和值
                    const std::string& key = key_value_list[i][j].first;
                    const int& value = key_value_list[i][j].second;
                    // 将值添加到对应键的对象中
                    json_obj["blocks"][i][j] = nlohmann::json::array();
                    json_obj["blocks"][i][j].push_back(std::stoi(key));
                    json_obj["blocks"][i][j].push_back(value);
                }
            }

            // 将JSON对象转换为字符串并写入json
            std::string json_str = json_obj.dump();
            std::ofstream cfile(key_value_list_txt);
            if (!cfile.is_open()) {
                std::cerr << "无法打开文件" << std::endl;
                return 1;
            }
            cfile << json_str;
            cfile.close();
        }

        return 0;
    }
}
