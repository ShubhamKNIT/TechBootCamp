#include <torch/extension.h>

torch::Tensor add_cpu(torch::Tensor a, torch::Tensor b) {
    return a + b;
}