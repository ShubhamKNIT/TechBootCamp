cmake_minimum_required(VERSION 3.12...3.18)
project(math_module)
add_subdirectory(pybind11)
pybind11_add_module(math_module module.cpp)