cmake_minimum_required(VERSION 3.28)
project(Cnew)

set(RUN_COVERAGE OFF CACHE BOOL "Compile with coverage options")

include_directories(${CMAKE_SOURCE_DIR})

set(CMAKE_CXX_STANDARD 23)

add_executable(Cnew main.cpp nbt.hpp)

set(Boost_DETAILED_FAILURE_MSG ON)
set(Boost_DEBUG ON)
set(Boost_USE_STATIC_LIBS ON)
set(Boost_MULTITHREADED ON)
set(Boost_USE_STATIC_RUNTIME OFF)

set(BOOST_ROOT "D:\\CodeVenv\\boost_1_85_0")
set(BOOST_INCLUDEDIR ${BOOST_ROOT}/include/boost-1_85)

set(BOOST_LIBRARY_DIR ${BOOST_ROOT}/lib)

MESSAGE(STATUS "boost root dir: " : ${BOOST_LIBRARYDIR})

set(Boost_ARCHITECTURE "-x64")

find_package(Boost 1.85.0 REQUIRED COMPONENTS
        container)

add_definitions(${Boost_LIB_DIAGNOSTIC_DEFINITIONS})

include_directories(${BOOST_INCLUDEDIR})

#target_link_libraries(cpp ${Boost_LIBRARIES})