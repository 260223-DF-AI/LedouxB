import torch
import numpy as np


np_array = np.array([[[1, 2, 3], [4, 5, 6]]])
tensor = torch.from_numpy(np_array)
print(tensor.shape)