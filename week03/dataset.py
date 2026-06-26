"""
- 使用 sklearn 的 make_classification 生成分类数据
- 自定义 Dataset 类（继承 torch.utils.data.Dataset)
- 创建 DataLoader,batch_size=32,shuffle=True
- 验证:iterate 一个 batch,打印 shape
"""

import torch
from torch.utils.data import Dataset, DataLoader
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split


class MyDataset(Dataset):
    def __init__(self, x, y):
        self.x = torch.tensor(x, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.long)

    def __len__(self):
        return len(self.x)

    def __getitem__(self, idx):
        return self.x[idx], self.y[idx]


def get_dataloaders(batch_size=32):
    x, y = make_classification(
        n_samples=1000,
        n_features=10,
        n_classes=2,
        random_state=42
    )

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    train_dataset = MyDataset(x_train, y_train)
    test_dataset = MyDataset(x_test, y_test)

    train_loader = DataLoader(
        train_dataset,
        batch_size=batch_size,
        shuffle=True
    )

    test_loader = DataLoader(
        test_dataset,
        batch_size=batch_size,
        shuffle=False
    )

    return train_loader, test_loader


if __name__ == "__main__":
    train_loader, test_loader = get_dataloaders()

    for batch_x, batch_y in train_loader:
        print("train batch_x:", batch_x.shape)
        print("train batch_y:", batch_y.shape)
        break

    for batch_x, batch_y in test_loader:
        print("test batch_x:", batch_x.shape)
        print("test batch_y:", batch_y.shape)
        break