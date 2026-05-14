#include <torch/extension.h>
#include <cuda.h>
#include <cuda_runtime.h>

__global__ void add_kernel(
    const float* a,
    const float* b,
    float* c,
    int n)
{
    int idx = blockIdx.x * blockDim.x + threadIdx.x;

    if (idx < n) {
        c[idx] = a[idx] + b[idx];
    }
}

torch::Tensor add_cuda(
    torch::Tensor a,
    torch::Tensor b)
{
    auto c = torch::zeros_like(a);

    int n = a.numel();

    int threads = 256;
    int blocks = (n + threads - 1) / threads;

    add_kernel<<<blocks, threads>>>(
        a.data_ptr<float>(),
        b.data_ptr<float>(),
        c.data_ptr<float>(),
        n);

    return c;
}