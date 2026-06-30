#分词、建立词表、文本向量化
import re
import torch

from numpy import dtype
from collections import Counter

def tokenize(text: str) -> list[str]:
    """
    将英文文本转换成单词列表。
    示例："I Love This World!" 
    -> ["i", "love","this","world"]
    """
    text = text.lower()
    tokens = re.findall(r"[a-zA-Z]+", text)#在字符串中找出英文单词，其中的正则表达式作用是把一句话
    return tokens

def build_vocab(texts: list[str]) -> dict[str, int]:
    """
    根据训练文本建立此表
    参数:   texts:所有的训练文本
            min_freq:单词至少出现多少次才加入词表
    返回:   单词到整数编号的映射
    """
    word_counter = Counter()

    for text in texts:
        tokens = tokenize(text)
        word_counter.update(tokens)
    
    #专门留给未知单词
    vocab = {"<unk>": 0}

    #排序可以让每次运行建立出来的词表顺序一致
    for word in sorted(word_counter.keys()):
        vocab[word] = len(vocab)

    return vocab

def text_to_bow(text: str, vocab: dict[str, int])-> torch.Tensor:
    """
    将文本转换为 Bag-of-Words 向量。

    向量长度等于词表大小。
    每个位置表示对应单词在文本中出现的次数。
    """
    tokens = tokenize(text)

    vector = torch.zeros(len(vocab), dtype=torch.float32)

    for token in tokens:
        index = vocab.get(token, vocab["<unk>"])
        vector[index] += 1
    return vector