import torch
import my_mps_extension

device = "mps"

a = torch.rand(10, device=device)
b = torch.rand(10, device=device)

c = my_mps_extension.add(a, b)

print(c)