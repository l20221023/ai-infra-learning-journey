import torch

# 1. 生成数据
X = torch.randn(100, 1)
true_w, true_b = 2.0, 0.5
y = true_w * X + true_b + 0.1 * torch.randn(100, 1)

# 2. 初始化参数
w = torch.randn(1, requires_grad=True)
b = torch.zeros(1, requires_grad=True)

# 3. 训练循环
lr = 0.1
for epoch in range(100):
    y_pred = w * X + b
    loss = ((y_pred - y) ** 2).mean()
    loss.backward()
    with torch.no_grad():
        w -= lr * w.grad
        b -= lr * b.grad
        w.grad.zero_()
        b.grad.zero_()
    if epoch % 10 == 0:
        print(f"Epoch {epoch}, loss={loss.item():.4f}, w={w.item():.4f}")