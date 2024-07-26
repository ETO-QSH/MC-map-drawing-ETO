#include <fstream>
#include <iostream>
#include <sstream>
#include "nbt.hpp"

int main(int argc, char** argv) {
  // 检查命令行参数数量
  if (argc != 5) {
    std::cerr << "Usage: " << argv[0] << " -p <filePath> -n <mapNum> " << std::endl;
    return -1;
  }
  
  // 解析命令行参数
  std::string filePath;
  int n = 1;

  for (int i = 1; i < argc; ++i) {
    if (strcmp(argv[i], "-p") == 0) {
      filePath = argv[++i];
    } else if (strcmp(argv[i], "-n") == 0) {
      char* end;
      n = static_cast<int>(strtol(argv[++i], &end, 10));
      if (*end != '\0') {
        std::cerr << "Error: Invalid number of nearest colors specified." << std::endl;
        return -1;
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
      return 1;
    }

    // 写入NBT数据
    outFile << oss.str();
    outFile.close();

    return 0;
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
      return 1;
    }

    // 编码并写入NBT数据
    nbtData.encode(outFile);
    outFile.close();

    return 0;
  }

}