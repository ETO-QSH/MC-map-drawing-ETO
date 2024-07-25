cmake_minimum_required(VERSION 3.28)
project(Cmap)
add_definitions( -g -ggdb -O0 )

set(CMAKE_CXX_STANDARD 20)
set(OpenCV_DIR "D:\\CodeVenv\\opencv\\mingw-build\\install")
find_package(OpenCV REQUIRED)
find_package (Eigen3 3.3 REQUIRED NO_MODULE)
include_directories(${OpenCV_INCLUDE_DIRS})
set(OpenCV_LIBS opencv_core opencv_imgproc opencv_highgui opencv_imgcodecs)
add_executable(Cmap main.cpp
                    KDTree.cpp
               allhpp/KDTree.hpp
               allhpp/CIEDE2000.hpp
               allhpp/RGB_to_XYZ.hpp
               allhpp/XYZ_to_Lab.hpp
)

target_link_libraries(Cmap ${OpenCV_LIBS})
target_link_libraries (Cmap Eigen3::Eigen)