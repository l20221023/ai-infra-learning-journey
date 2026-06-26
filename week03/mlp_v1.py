"""
- 定义一个 MLP 类（继承 nn.Module）
- 两个隐藏层，ReLU 激活
- forward() 方法
"""

import torch
import torch.nn as nn


class MLP(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()

        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, hidden_dim)
        self.fc3 = nn.Linear(hidden_dim, output_dim)

        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)
        return x


if __name__ == "__main__":
    model = MLP(input_dim=10, hidden_dim=32, output_dim=2)
    print(model)

    x = torch.randn(1, 10)
    y = model(x)

    print("input shape:", x.shape)
    print("output shape:", y.shape)
    print("output:", y)