cmake_minimum_required(VERSION 3.15)
project(pyhashcat)

add_library(pyhashcat pyhashcat/pyhashcat.c)

set(CMAKE -std=c99 -DWITH_BRAIN -Wimplicit-function-declaration)
set(PYTHON_VERSION "3")

if(${PYTHON_VERSION} EQUAL "3")
    find_package(Python3 COMPONENTS Interpreter Development)
elseif(${PYTHON_VERSION} EQUAL "2")
    find_package(Python COMPONENTS Interpreter Development)
endif()

include_directories(hashcat/include)
include_directories(hashcat/deps/OpenCL-Headers)
include_directories(hashcat/OpenCL)
include_directories(hashcat)
include_directories(hashcat/deps/LZMA-SDK/C)
include_directories(hashcat/deps/zlib)
include_directories(hashcat/deps/zlib/contrib/minizip)

target_link_libraries(pyhashcat hashcat)
