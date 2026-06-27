import torch

from src.model import SentimentMLP

checkpoint = torch.load("checkpoint.pth", map_location="cpu",)

model = SentimentMLP(
    input_dim = checkpoint["input_dim"],
    hidden_dim=checkpoint["hidden_dim"],
    output_dim = checkpoint["output_dim"]
)

model.load_state_dict(checkpoint["model_state_dict"])

model.eval()

vocab = checkpoint["vocab"]

print("模型加载成功")
print("词表大小：", len(vocab))
print("原测试准确率：", checkpoint["test_accuracy"])