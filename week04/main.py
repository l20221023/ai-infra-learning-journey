#组装数据和模型，测试 forward
from numpy import average
from numpy.testing._private.extbuild import build_and_import_extension
from src.preprocess import build_vocab, tokenize, text_to_bow
from src.dataset import SentimentDataset
from torch.utils.data import DataLoader
from src.model import SentimentMLP
from torch import nn
from eval import evaluate
import matplotlib.pyplot as plt
import torch


texts = [
    "I love this movie",
    "This film is wonderful",
    "I hate this movie",
    "This film is terrible",
]

labels = [1, 1, 0, 0]

test_texts = [
    "I love this film",
    "This movie is wonderful",
    "I hate this film",
    "This movie is terrible",
]

test_labels = [1, 1, 0, 0]

dataset = SentimentDataset(test_texts, test_labels)
test_dataset = SentimentDataset(test_texts, test_labels, vocab=dataset.vocab)

loader = DataLoader(dataset, batch_size=4, shuffle=True)
test_loader = DataLoader(dataset, batch_size=2, shuffle = False)
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

epoch_loss_sum = 0.0
loss_history = []
accuracy_history = []
num_epochs = 200

for epoch in range(num_epochs):
    model.train()

    total_loss = 0.0
    correct_count = 0
    sample_count = 0

    for batch_x, batch_y in loader:
        optimizer.zero_grad()

        logits = model(batch_x)
        loss = criterion(logits, batch_y)

        loss.backward()
        optimizer.step()

        #loss是零维Tensor，记录训练日志不需要保留计算图，调用item()可以得到普通Python浮点数，
        total_loss += loss.item()

        """注意这里total_loss并不严谨。更严谨的应该是：
        total_loss += loss.item() * batch_y.size(0)
        他所做的是将loss.item乘上样本数量，最后再除以总的样本数量获取真正平均值
        """

        predictions = torch.argmax(logits, dim = 1)
        correct = (predictions == batch_y).sum().item()
        #predictions == batch_y得到的是tensor[True,True,True,False]样例，.sum得到的是tensor(3),.item得到的是整数2

        correct_count += correct
        sample_count += batch_y.size(0)#表示获取第0个维度的长度。

    epoch_accuracy = correct_count / sample_count
    average_loss = total_loss / len(loader)
    
    #记录损失函数的参数
    loss_history.append(average_loss)
    accuracy_history.append(epoch_accuracy)

    if (epoch-1)%50 == 0:
        print(
            f"Epoch [{epoch + 1}/{num_epochs}], "
            f"Loss: {average_loss:.4f}, "
            f"Accuracy: {epoch_accuracy:.4f}"
        )
test_accuracy = evaluate(model, test_loader)

print(f"测试机 Accuracy:{ test_accuracy:.4f}")

plt.figure()

plt.plot(
    range(1, num_epochs + 1),
    loss_history,
)

plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training Loss Curve")

plt.savefig(
    "loss_curve.png",
    dpi =  150,
    bbox_inches="tight",
)

plt.close()

checkpoint = {
    "model_state_dict": model.state_dict(),
    "optimizer_state_dict": optimizer.state_dict(),
    "vocab": dataset.vocab,
    "input_dim": input_dim,
    "hidden_dim": hidden_dim,
    "output_dim": output_dim,
    "num_epochs": num_epochs,
    "loss_history": loss_history,
    "accuracy_history": accuracy_history,
    "test_accuracy": test_accuracy,
}

torch.save(
    checkpoint,
    "checkpoint.pth",
)

print("模型已保存到 checkpoint.pth")

if __name__ == "__main__":
    main()