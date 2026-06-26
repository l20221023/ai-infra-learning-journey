"""
- 输入特征从1维改为5维
- 加入 L2 正则化,MSE+lambda(平方求和)
- 画出 loss 下降曲线（用 matplotlib 或直接打印）
- 写 README.md：说明这个脚本做了什么，怎么运行
"""

import torch
import matplotlib.pyplot as plt

X = torch.randn(100, 5)
true_w = torch.tensor([
    [2.0],
    [1.0],
    [-1.0],
    [0.5],
    [3.0]
])
true_b = 0.5
y_true = X @ true_w + true_b

w = torch.randn((5, 1), requires_grad = True)
b = torch.rand(1, requires_grad = True)


l2_lambda = 0.01
lr = 0.1
losses = []

for epoch in range(100):
    y = X @ w + b
    mse = ((y_true - y)**2).mean()
    l2_loss = (w**2).sum()
    loss = mse + l2_lambda*l2_loss
    loss.backward()
    with torch.no_grad():
        w -= lr * w.grad
        b -= lr * b.grad
        w.grad.zero_()
        b.grad.zero_()
    losses.append(loss.item())
    if epoch % 10 == 0:
        print(
            f"Epoch {epoch:3d} | "
            f"Loss={loss.item():.6f}"
        )


# ==========================
# 结果
# ==========================

print("\n真实参数：")
print(true_w.squeeze())

print("\n学习参数：")
print(w.detach().squeeze())

print("\n真实偏置：", true_b)
print("学习偏置：", b.item())

# ==========================
# Loss 曲线
# ==========================

plt.plot(losses)

plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training Loss")

plt.show()