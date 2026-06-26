"""
```
□ 写 eval.py：
    model.eval()
    with torch.no_grad():
        # 在测试集上计算 accuracy

□ 加入 checkpoint 保存和加载：
    torch.save(model.state_dict(), 'checkpoint.pth')
    model.load_state_dict(torch.load('checkpoint.pth'))

□ 验证：保存后重新加载，accuracy 一致
"""
#一个函数只能干一件事
#通常在eval开始的时候导入model：torch.load("checkpoint.pth")
import torch
import mlp_v1 as mlp
from dataset import get_dataloaders

def evaluate(model, test_loader):#负责预测→统计正确数量→计算accuracy→返回accuracy
    model.eval()#进入测试模式

    correct = 0 #统计正确了的数量
    total = 0 #统计总数

    with torch.no_grad():
        for X_batch,y_batch in test_loader:
            out = model(X_batch)
            pred = torch.argmax(out, dim=1)#得分最高的类别

            correct += (pred == y_batch).sum().item()#预测正确时的得分综合
            total += y_batch.size(0)#总共有多少个样本
    
    accuracy = correct / total
    return accuracy


if __name__ == "__main__":
    _, test_loader = get_dataloaders()

    model = mlp.MLP(input_dim=10, hidden_dim=32, output_dim=2)
    model.load_state_dict(torch.load("checkpoint.pth"))

    acc = evaluate(model, test_loader)
    print(f"Accuracy: {acc:.4f}")