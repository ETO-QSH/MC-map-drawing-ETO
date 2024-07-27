#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <regex>
#include "nbt.hpp"

void handlePN(int argc, char** argv);
void handleFC(int argc, char** argv);

int main(int argc, char** argv) {
    // 检查命令行参数数量
    if (argc < 5) {
        std::cerr << "Usage: " << argv[0] << " -p <filePath> -n <mapNum> " << std::endl;
        std::cerr << "Usage: " << argv[0] << " -f <filePath> -c <pivixColor> " << std::endl;
        return -1;
    }

    // 解析命令行参数
    for (int i = 1; i < argc; ++i) {
        if (strcmp(argv[i], "-p") == 0) {
            handlePN(argc, argv);
        } else if (strcmp(argv[i], "-f") == 0) {
            handleFC(argc, argv);
        }
    }

    return 0;
}

void handlePN(int argc, char** argv) {
    // 解析 -p 和 -n 参数
    int n = 1;
    std::string filePath;

    for (int i = 1; i < argc; ++i) {
        if (strcmp(argv[i], "-p") == 0) {
            filePath = argv[++i];
        } else if (strcmp(argv[i], "-n") == 0) {
            char* end;
            n = static_cast<int>(strtol(argv[++i], &end, 10));
            if (*end != '\0') {
                std::cerr << "Error" << std::endl;
            }
        }
    }

    try {
        // 创建NBT根节点实例
        nbt::NBT root;

        // 以二进制模式打开文件
        std::ifstream nbtFile(filePath, std::ios::binary);

        // 解码NBT数据到根节点
        root.decode(nbtFile);
        nbtFile.close();

        // 打印NBT数据
        //root.print(std::cout);

        const auto& compound = root.data->tags.find("data");
        const auto& tagCompound = std::get<nbt::TagCompound>(compound->second);
        for (auto& [key, tag] : tagCompound) {
            if (key == "map") {
                // 将新的TagCompound赋值给非const引用
                auto& nonConstTagCompound = const_cast<nbt::TagCompound&>(tagCompound);
                nonConstTagCompound[key] = std::get<std::int32_t>(tag) + n;
            }
        }

        std::ostringstream oss;
        root.encode(oss);

        // 将编码后的数据写入到文件中
        std::ofstream outFile(filePath, std::ios::binary);
        if (!outFile) {
            std::cerr << "can't write" << std::endl;
        }

        // 写入NBT数据
        outFile << oss.str();
        outFile.close();
    }

    catch (...) {
        // 创建一个新的NBT数据结构
        nbt::NBT nbtData("", nbt::TagCompound{{
            {"DataVersion", nbt::TagInt{0}},
            {"data", nbt::TagCompound{
              {"map", nbt::TagInt{n-1}
              }}},
            }});

        // 将NBT数据写入到文件
        std::ofstream outFile(filePath, std::ios::binary);
        if (!outFile) {
            std::cerr << "can't write" << std::endl;
        }

        // 编码并写入NBT数据
        nbtData.encode(outFile);
        outFile.close();
    }
}

void handleFC(int argc, char** argv) {
    // 解析 -f 和 -c 参数
    std::string filePath;
    std::string pivixColor;

    for (int i = 1; i < argc; ++i) {
        if (strcmp(argv[i], "-f") == 0) {
            filePath = argv[++i];
        } else if (strcmp(argv[i], "-c") == 0) {
            pivixColor = argv[++i];
        }
    }

    try {
        // 没意义，但是少了就出问题，而且必须用try
        throw "ETO";
    }

    catch (...) {
        // 读取并创建一个 std::vector<uint8_t> 类型的变量
        std::ifstream file(pivixColor);
        std::vector<uint8_t> pivix_color;
        std::string line;
        std::regex hex_regex("0x[0-9A-Fa-f]{2}");

        while (std::getline(file, line)) {
            std::smatch match;
            std::string::const_iterator searchStart(line.cbegin());
            while (std::regex_search(searchStart, line.cend(), match, hex_regex)) {
                std::string hex_value = match[0];
                auto value = static_cast<uint8_t>(std::stoi(hex_value, nullptr, 16));
                pivix_color.push_back(value);
                searchStart = match.suffix().first;
            }
        }

        file.close();

        // 将 std::vector<uint8_t> 转换为 std::vector<signed char>
        std::vector<signed char> signed_char_color(pivix_color.begin(), pivix_color.end());

        // 创建一个 TagByteArray 类型的变量
        nbt::TagByteArray tag_byte_array(signed_char_color.begin(), signed_char_color.end());

        // 创建一个新的NBT数据结构
        nbt::NBT nbtData("", nbt::TagCompound{{
            {"DataVersion", nbt::TagInt{3953}},
            {"data", nbt::TagCompound{
              {"banners", nbt::TagList{}},
              {"colors", nbt::TagByteArray{tag_byte_array}},
              {"dimension", nbt::TagString{"minecraft:overworld"}},
              {"frames", nbt::TagList{}},
              {"locked", nbt::TagByte{1}},
              {"scale", nbt::TagByte{0}},
              {"trackingPosition", nbt::TagByte{0}},
              {"unlimitedTracking", nbt::TagByte{0}},
              {"xCenter", nbt::TagInt{0}},
              {"zCenter", nbt::TagInt{0}},
              }},
            }});

        // 将NBT数据写入到文件
        std::ofstream outFile(filePath, std::ios::binary);
        if (!outFile) {
            std::cerr << "can't write" << std::endl;
        }

        // 编码并写入NBT数据
        nbtData.encode(outFile);
        outFile.close();
    }
}