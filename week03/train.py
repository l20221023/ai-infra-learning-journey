"""
写完整训练循环 train.py:
model = MLP(...)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
criterion = nn.CrossEntropyLoss()

for epoch in range(50):
    model.train()#进入训练模式，以后Dropout、BatchNorm会用到
    for X_batch, y_batch in train_loader:
        optimizer.zero_grad()
        out = model(X_batch)
        loss = criterion(out, y_batch)
        loss.backward()
        optimizer.step()
    # 每10个epoch打印一次 loss

□ 运行通过,loss 要能明显下降。数据→MLP→预测值→Loss→反向传播→更新参数→更好的预测
"""

import torch
import torch.nn as nn
#from torch.optim import optimizer
from dataset import get_dataloaders
from eval import evaluate
import mlp_v1 as mlp


#创建模型：此处的输入和输出对应着自动生成的XY数据中样本维度？标签维度？
#output_dim = 2表示类别数量，对应n_classes = 2
model = mlp.MLP(input_dim=10, hidden_dim=32, output_dim=2)
#Adam负责根据梯度修改这些权重和偏置值
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
criterion = nn.CrossEntropyLoss()#计算预测和真是答案之间的差距

train_loader,test_loader = get_dataloaders()#这样更灵活


for epoch in range(50):
    model.train()#进入训练模式，以后Dropout、BatchNorm会用到

    for X_batch, y_batch in train_loader:
        optimizer.zero_grad()
        out = model(X_batch)
        loss = criterion(out, y_batch)

        loss.backward()
        optimizer.step()
    # 每10个epoch打印一次 loss
    if (epoch + 1) % 10 == 0:
        print(f"Epoch [{epoch+1}/50], Loss: {loss.item():.4f}")

_, test_loader = get_dataloaders()
train_acc = evaluate(model, test_loader)
print(f"Accuracy before saving: {train_acc:.4f}")

torch.save(model.state_dict(), "checkpoint.pth")

torch.save(model.state_dict(), "checkpoint.pth")
print("Model saved to checkpoint.pth")

