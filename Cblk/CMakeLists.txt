cmake_minimum_required(VERSION 3.28)
project(Cblk)

add_definitions( -g -ggdb -O0 )

set(CMAKE_CXX_STANDARD 26)
set(OpenCV_DIR "D:\\CodeVenv\\opencv\\mingw-build\\install")

find_package(OpenCV REQUIRED)

include_directories(${OpenCV_INCLUDE_DIRS})

set(OpenCV_LIBS opencv_core opencv_imgproc opencv_highgui opencv_imgcodecs)

add_executable(Cblk main.cpp)

target_link_libraries(Cblk ${OpenCV_LIBS})
