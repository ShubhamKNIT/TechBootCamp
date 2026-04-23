#include <pybind11//pybind11.h>

namespace py = pybind11;

int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

PYBIND11_MODULE(math_module, m) {
    m.doc() = "math module";

    m.def("add", &add, "A function which adds two numbers", py::arg("a"), py::arg("b"));
    m.def("subtract", &subtract, "A function which subtracts two numbers", py::arg("a"), py::arg("b"));
}