#import torch
#print(torch.cuda.is_available())
#print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else "CPU only")
"""
□ 给 MLP 加上混合精度训练（AMP）：
    from torch.cuda.amp import autocast, GradScaler
    scaler = GradScaler()
    ...
□ 对比有无 AMP 的训练速度（如果有 GPU）
"""
import torch
from dataset import get_dataloaders
import mlp_v1 as mlp
import torch.nn as nn

train_loader,__ = get_dataloaders()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = mlp.MLP(input_dim=10, hidden_dim=32, output_dim=2).to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
criterion = nn.CrossEntropyLoss()

use_amp = device.type == "cuda"
scaler = torch.amp.GradScaler("cuda", enabled=use_amp)

for epoch in range(50):
    model.train()

    for X_batch, y_batch in train_loader:
        X_batch = X_batch.to(device)
        y_batch = y_batch.to(device)

        optimizer.zero_grad()

        with torch.amp.autocast("cuda", enabled=use_amp):#负责让部分计算自动用低精度
            out = model(X_batch)
            loss = criterion(out, y_batch)

        scaler.scale(loss).backward()#负责放大loss，避免FP16梯度太小
        scaler.step(optimizer)#接着两行负责安全更新参数。
        scaler.update()

    if (epoch + 1) % 10 == 0:
        print(f"Epoch [{epoch+1}/50], Loss: {loss.item():.4f}")