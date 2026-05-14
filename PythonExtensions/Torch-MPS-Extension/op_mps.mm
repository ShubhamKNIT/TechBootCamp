#import <Metal/Metal.h>
#import <Foundation/Foundation.h>

#include <torch/extension.h>

torch::Tensor add_mps(torch::Tensor a, torch::Tensor b) {
    return a + b;
}