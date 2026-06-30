#定义PyTorch Dataset
import csv
from pathlib import Path

import torch
from torch.utils.data import Dataset

from src.preprocess import build_vocab,text_to_bow

def load_sentiment_csv(csv_path: str | Path) -> tuple[list[str], list[int]]:
    """
    从CSV文件读取文本和标签。
    csv必须包含: test, label
    """
    csv_path = Path(csv_path)
    if not csv_path.exists():
        raise FileNotFoundError(f"数据文件不存在:{csv_path}")
    
    texts:list[str] = []
    labels:list[int] = []

    with csv_path.open(model="r",encoding="utf-8",newline="") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            raise ValueError("CSV 文件缺少表头")

        required_columns = {"text", "label"}

        if not required_columns.issubset(reader.fieldnames):
            raise ValueError(
                "CSV 文件必须包含text 和 label 两列"
            )
        
        for row_number, row in enumerate(reader, start=2):
            text = row["text"].strip()

            if not text:
                raise ValueError(f"CSV 第{row_number}行文本为空")
            
            try: 
                label = int(row["label"])
            except ValueError as error:
                raise ValueError(f"CSV 第{row_number}行标签不是整数")from error
            
            if label not in{0, 1}:
                raise ValueError(f"CSV 第{row_number}行标签必须是0 或 1")
            
            texts.append(text)
            labels.append(label)

    if not texts:
        raise ValueError(f"CSV文件没有有效样本: {csv_path}")
    
    return texts, labels


class SentimentDataset(Dataset):
    #保存数据,texts是话、labels指的是每句话的情绪正负
    def __init__(self, 
        texts: list[str], 
        labels: list[int] , 
        vocab: dict[str, int] | None=None
    ) -> None:

        super().__init__()

        if len(texts)!=len(labels):
            raise ValueError("texts 和 labels 的数量必须一致")
        
        if len(texts) == 0:
            raise ValueError("数据集不能为空")
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
    def __getitem__(self, index: int) -> tuple[torch.Tensor, torch.Tensor]:
        text = self.texts[index]
        label = self.labels[index]

        x = text_to_bow(text, self.vocab)
        y = torch.tensor(label, dtype=torch.long)

        return x, y