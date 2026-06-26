#定义MLP，他要完成的任务是，将输入模型的向量dim经过计算，转换成output的dim

import torch
from torch import nn

class SentimentMLP(nn.Module):

    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int):
        # 定义网络层
        super().__init__()

        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # 定义前向传播的路径
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)

        return x