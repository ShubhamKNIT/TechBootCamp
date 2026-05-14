#include <torch/extension.h>

torch::Tensor add_cpu(torch::Tensor a, torch::Tensor b);
torch::Tensor add_mps(torch::Tensor a, torch::Tensor b);

torch::Tensor add(torch::Tensor a, torch::Tensor b) {
    if (a.device().is_mps()) {
        return add_mps(a, b);
    } else {
        return add_cpu(a, b);
    }
}

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
    m.def("add", &add, "A function that adds two tensors");
}