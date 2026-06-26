"""
- (32, 128) @ (128, 64) 结果是什么？
- (32, 1, 64) 和 (1, 10, 64) broadcast 后各是什么形状？
- 用 einsum 实现矩阵乘法
- 用 view 和 reshape 改变形状，区别是什么？
"""

import torch
a = torch.ones(32, 128)
b = torch.ones(128, 64)
M = a @ b

print(f"M.shape: {M.shape}")

