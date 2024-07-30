cmake_minimum_required(VERSION 3.28)
project(Cset)

add_definitions( -g -ggdb -O0 )

set(CMAKE_CXX_STANDARD 26)

add_executable(Cset main.cpp json.hpp)
