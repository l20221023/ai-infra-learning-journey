#组装数据和模型，测试 forward
from numpy.testing._private.extbuild import build_and_import_extension
from src.preprocess import build_vocab, tokenize, text_to_bow
from src.dataset import SentimentDataset
from torch.utils.data import DataLoader
from src.model import SentimentMLP
from torch import nn
import torch

texts = [
    "I love this movie",
    "This film is wonderful",
    "I hate this movie",
    "This film is terrible",
]

labels = [1, 1, 0, 0]

dataset = SentimentDataset(texts, labels)

loader = DataLoader(dataset, batch_size=2, shuffle=True)

#这里iter()的作用：从一个“可迭代对象”中创建迭代器
#next()：向迭代器索要下一项数据，但是在正常训练中用for循环多一些
input_dim = len(dataset.vocab)
hidden_dim = 8
output_dim = 2

model = SentimentMLP(
    input_dim = input_dim, 
    hidden_dim= hidden_dim, 
    output_dim= output_dim
)

optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()
num_epochs = 50
for epoch in range(num_epochs):
    for batch_x, batch_y in loader:
        optimizer.zero_grad()

        logits = model(batch_x)
        loss = criterion(logits, batch_y)

        loss.backward()

        #必须由detach().clone()因为在python中只是=的话就是将内存的地址赋值给了新变量，而不是内容
        #如果想赋值内容就得detach().clone()
        weight_before = model.fc1.weight.detach().clone()
        optimizer.step()

        weight_after = model.fc1.weight.detach().clone()

        parameter_change = weight_after - weight_before

        print("参数变化量：")
        print(parameter_change)

        print("参数变化量绝对值之和：")
        print(parameter_change.abs().sum().item())