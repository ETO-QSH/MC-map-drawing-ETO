#include <iostream>
#include <fstream>
#include <string>
#include <random>
#include "json.hpp"

// 生成随机数的函数
std::string random_string_from_list(const nlohmann::json& json_obj, const std::string& key) {
    // 检查键是否存在于json对象中
    if (json_obj.find(key) != json_obj.end() && json_obj[key].is_array()) {
        // 获取与键关联的值（字符串列表）
        const auto& list = json_obj.at(key);

        // 检查列表是否为空
        if (!list.empty()) {
            // 创建随机数生成器
            std::random_device rd; // 非确定性随机数生成器
            std::mt19937 gen(rd()); // 伪随机数生成器，使用随机设备作为种子

            // 生成随机索引
            std::uniform_int_distribution<std::size_t> dist(0, list.size() - 1);
            std::size_t random_index = dist(gen);

            // 返回随机选中的字符串
            return list[random_index];
        }
    }

    // 如果键不存在或列表为空，返回空气
    return "air";
}

int main(int argc, char** argv) {
    // 检查命令行参数数量
    if (argc != 13) {
        std::cerr << "Usage: " << argv[0] << " -b <BlockList> -k <key_value_list> -o <block_List> -x <xchunk> -z <zchunk> -y <flat>" << std::endl;
        return -1;
    }

    // 解析命令行参数
    int flat = 30, xchunk = 0, zchunk = 0;
    std::string block_List;
    std::string BlockList;
    std::string key_value_list;

    for (int i = 1; i < argc; ++i) {
        if (strcmp(argv[i], "-b") == 0) {
            BlockList = argv[++i];
        } else if (strcmp(argv[i], "-k") == 0) {
            key_value_list = argv[++i];
        } else if (strcmp(argv[i], "-o") == 0) {
            block_List = argv[++i];
        } else if (strcmp(argv[i], "-x") == 0) {
            char* end;
            xchunk = static_cast<int>(strtol(argv[++i], &end, 10));
            if (*end != '\0') {
                std::cerr << "ErrorX!" << std::endl;
                return -1;
            }
        } else if (strcmp(argv[i], "-y") == 0) {
            char* end;
            flat = static_cast<int>(strtol(argv[++i], &end, 10));
            if (*end != '\0') {
                std::cerr << "ErrorY" << std::endl;
                return -1;
            }
        } else if (strcmp(argv[i], "-z") == 0) {
            char* end;
            zchunk = static_cast<int>(strtol(argv[++i], &end, 10));
            if (*end != '\0') {
                std::cerr << "ErrorZ" << std::endl;
                return -1;
            }
        }
    }

    // 下辈子有机会一定去搞懂不是
    try {
        throw "ETO";
    }

    catch (...) {

        // 创建一个新的空JSON对象
        nlohmann::json new_json;

        // 打开文件
        std::ifstream json_file(key_value_list);
        if (!json_file.is_open()) {
            std::cerr << "ERROR!" << std::endl;
            return 1;
        }
        std::ifstream block_file(BlockList);
        if (!json_file.is_open()) {
            std::cerr << "ERROR!" << std::endl;
            return 1;
        }

        // 解析JSON文件
        try {
            nlohmann::json p;
            block_file >> p;

            for (const auto& block : p["BlockList"]) {
                // 获取id值
                std::string id = block["id"].get<std::string>();

                // 提取冒号右边的部分
                size_t colon_pos = id.find(':');
                if (colon_pos != std::string::npos) {
                    // 提取内层信息
                    std::string id_right_part = id.substr(colon_pos + 1);
                    std::string color_str = std::to_string(block["color"].get<int>());

                    // 如果键不存在于new_json中，则创建一个空列表
                    if (new_json.find(color_str) == new_json.end()) {
                        new_json[color_str] = nlohmann::json::array();
                    }

                    // 将id的右边部分添加到对应color键的列表中
                    new_json[color_str].push_back(id_right_part);
                }
            }

        } catch (nlohmann::json::parse_error& e) {
            std::cerr << "error: " << e.what() << std::endl;
            return 1;
        }

        // 用于存储生成的二维数组
        std::vector<std::tuple<std::string, int, int, int>> generated_blocks;

        // 解析JSON文件
        try {
            nlohmann::json j;
            json_file >> j;
            int avar = flat;

            auto blocks = j["blocks"];
            for (int row = 0; row < blocks.size(); ++row) {
                for (int col = 0; col < blocks[row].size(); ++col) {
                    std::string bkey = std::to_string(blocks[row][col][0].get<int>());
                    int bvar = blocks[row][col][1].get<int>();

                    // 调用函数获取随机字符串
                    std::string random_str = random_string_from_list(new_json, bkey);

                    // 计算数组中每个元素的值
                    int first_value = (xchunk + 1) * 16 - row;
                    int second_value = flat + bvar;
                    int third_value = (zchunk + 1) * 16 - col;

                    // 将计算结果添加到数据中
                    generated_blocks.emplace_back(random_str, first_value, second_value, third_value);

                    // 特殊处理水方块，挖空下面的方块，可能会漏水
                    if (bkey == "12") {
                        if (bvar == avar) {
                            for (int q = 1; q < 5; ++q) {
                                generated_blocks.emplace_back("air", first_value, second_value - q, third_value);
                            }
                        } else if (bvar < avar) {
                            for (int q = 1; q < 7; ++q) {
                                generated_blocks.emplace_back("air", first_value, second_value - q, third_value);
                            }
                        }
                    }

                    // 记录纹理走势
                    avar = bvar;
                }
            }

            // 将生成的二维数组转换为JSON格式
            nlohmann::json generated_json = nlohmann::json::array();
            for (const auto& row : generated_blocks) {
                generated_json.push_back(row);
            }

            // 将JSON对象转换为字符串并写入json
            std::string json_str = generated_json.dump();
            std::ofstream cfile(block_List);
            if (!cfile.is_open()) {
                std::cerr << "无法打开文件" << std::endl;
                return 1;
            }
            cfile << json_str;
            cfile.close();

        } catch (nlohmann::json::parse_error& e) {
            std::cerr << "error: " << e.what() << std::endl;
            return 1;
        }

        // 关闭文件
        block_file.close();
        json_file.close();

        return 0;
    }
}
