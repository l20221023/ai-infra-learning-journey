# Sentiment Classification with MLP and Bag-of-Words

这是一个基于 PyTorch 实现的文本情感分类项目。

项目使用 Bag-of-Words 将文本转换为固定长度向量，
然后使用多层感知机 MLP 判断文本情感属于积极还是消极。

## 项目结构

- `data/`：训练集和测试集
- `src/preprocess.py`：文本预处理和 Bag-of-Words
- `src/dataset.py`：PyTorch Dataset
- `src/model.py`：MLP 模型
- `main.py`：数据与模型 forward 测试

## 标签定义

- `0`：消极
- `1`：积极

## 运行方式

```bash
python main.py