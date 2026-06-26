"""
 创建 x = torch.tensor(3.0, requires_grad=True)
    - 计算 y = x**2 + 2*x + 1
    - y.backward()
    - 打印 x.grad，验证是否等于 2x+2=8
    - 创建一个 (3,3) 矩阵，做矩阵乘法，backward
    - 打印每一步的 grad_fn，理解计算图
"""

import torch as th

# 标量自动求导
# x = th.tensor(3.0, requires_grad=True)

y = x**2 + 2*x + 1

y.backward()

print(f"x.grad: {x.grad}")

# 矩阵乘法
a = th.arange(0, 9, dtype=th.float32).reshape(3, 3)

b = th.tensor([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
], dtype=th.float32, requires_grad=True)

c = a @ b

print("c:")
print(c)

loss = c.sum()


print(f"c:{ c.shape}\n")

print("loss:", loss)

loss.backward()

print("b.grad:")
print(b.grad)

print("loss.grad_fn:")
print(loss.grad_fn)