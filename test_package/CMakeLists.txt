project(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)

set(CMAKE_VERBOSE_MAKEFILE TRUE)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

if(APPLE)
set ( CMAKE_EXE_LINKER_FLAGS "-pagezero_size 10000 -image_base 100000000" )
endif()

add_executable(example example.cpp)
target_link_libraries(example ${CONAN_LIBS})
