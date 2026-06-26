"""
- 用数值微分（有限差分法）手动验证 PyTorch 的 grad 是否正确
- 公式：f'(x) ≈ (f(x+ε) - f(x-ε)) / (2ε)
- 对比数值梯度和 autograd 梯度，误差应该 < 1e-5
"""

import torch
#导入自变量x,本测试要求通过autograd和数值的梯度之间计算差异
x = torch.tensor(3.0, requires_grad = True)

#先定义一个公式，开始计算自动求导
y = x**2 + 2*x + 1

y.backward() #此处开始反向传播

autograd_grad = x.grad.item() #

# numerical gradient
eps = 1e-5

x1 = x + eps
x2 = x - eps

y1 = x1**2 + 2*x1 + 1
y2 = x2**2 + 2*x2 + 1
num_grad = (y1 - y2)/(2*eps)

print("autograd:", autograd_grad)
print("numerical:", num_grad)

print("error:", abs(autograd_grad - num_grad))
