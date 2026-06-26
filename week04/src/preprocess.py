import re
import torch

from numpy import dtype
from collections import Counter

def tokenize(text: str) -> list[str]:
    text = text.lower()
    tokens = re.findall(r"[a-zA-Z]+", text)#在字符串中找出英文单词，
    return tokens

def build_vocab(texts: list[str]) -> dict[str, int]:
    word_counter = Counter()

    for text in texts:
        tokens = tokenize(text)
        word_counter.update(tokens)
    
    vocab = {"<unk>": 0}

    for word in sorted(word_counter.keys()):
        vocab[word] = len(vocab)

    return vocab

def text_to_bow(text: str, vocab: dict[str, int])-> torch.Tensor:
    tokens = tokenize(text)

    vector = torch.zeros(len(vocab), dtype=torch.float32)

    for token in tokens:
        index = vocab.get(token, vocab["<unk>"])
        vector[index] += 1
    return vector