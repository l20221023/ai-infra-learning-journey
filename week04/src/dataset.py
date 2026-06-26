#定义PyTorch Dataset

import torch
from torch.utils.data import Dataset

from src.preprocess import build_vocab,text_to_bow


class SentimentDataset(Dataset):
    #保存数据
    def __init__(self, texts, labels, vocab=None) -> None:
        super().__init__()
        self.texts = texts
        self.labels = labels

        if vocab is None:
            self.vocab = build_vocab(texts)
        else:
            self.vocab = vocab
    #返回样本数量
    def __len__(self):
        return len(self.texts)
    
    #取出某条数据，转成Tensor，返回x，y
    def __getitem__(self, index):
        text = self.texts[index]
        label = self.labels[index]

        x = text_to_bow(text, self.vocab)
        y = torch.tensor(label, dtype=torch.long)

        return x, y