import torch

x = torch.rand(5, 3)
print(x)

torch.cuda.is_available()
torch.cuda.current_device()
torch.cuda.device_count()
torch.cuda.get_device_name(0)
