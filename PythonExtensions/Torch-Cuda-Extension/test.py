import torch
import my_extension

a = torch.rand(10, device='cuda')
b = torch.rand(10, device='cuda')

c = my_extension.add(a, b)

print(c)