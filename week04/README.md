# Sentiment Classification with MLP and Bag-of-Words

## 1. 项目简介

本项目使用 PyTorch 实现一个英文文本情感二分类模型。

模型首先使用 Bag-of-Words（BoW，词袋模型）将英文文本转换为固定长度的数值向量，再使用多层感知机（MLP）判断文本情感属于积极或消极。

标签定义：

* `0`：消极
* `1`：积极

本项目的主要目标是完整实践以下机器学习流程：

```text
原始文本
→ 分词
→ 使用训练集建立词表
→ Bag-of-Words 向量化
→ Dataset
→ DataLoader
→ MLP
→ 模型训练
→ 测试集评估
→ Checkpoint 保存和加载
```

## 2. 项目结构

```text
week04/
├── data/
│   ├── train.csv
│   └── test.csv
├── outputs/
│   ├── best_checkpoint.pth
│   ├── loss_curve.png
│   └── train_log.txt
├── src/
│   ├── __init__.py
│   ├── preprocess.py
│   ├── dataset.py
│   └── model.py
├── train.py
├── eval.py
├── requirements.txt
├── README.md
└── .gitignore
```

各文件职责：

* `data/train.csv`：训练数据。
* `data/test.csv`：测试数据。
* `src/preprocess.py`：分词、词表建立和 BoW 向量化。
* `src/dataset.py`：定义文本情感分类 Dataset。
* `src/model.py`：定义 MLP 模型。
* `train.py`：训练模型、记录指标、保存最佳 checkpoint 和 loss 曲线。
* `eval.py`：加载 checkpoint，并在测试集上重新计算准确率。
* `outputs/`：保存模型、图像和训练日志。

## 3. 数据格式

CSV 文件包含两列：

```csv
text,label
I love this movie,1
I hate this movie,0
```

其中：

* `text`：英文评论文本。
* `label`：情感类别，`0` 表示消极，`1` 表示积极。

词表只根据训练集建立。测试集复用训练阶段的词表，避免输入特征位置错位和测试数据泄漏。

## 4. 数据预处理

项目使用以下预处理流程：

1. 将英文文本转换为小写。
2. 使用正则表达式提取单词。
3. 使用训练集文本建立 `word -> index` 词表。
4. 将每条文本转换为长度为 `vocab_size` 的 BoW 向量。
5. 每个向量位置表示对应单词在文本中出现的次数。

例如，假设词表为：

```python
{
    "i": 0,
    "love": 1,
    "hate": 2,
    "movie": 3
}
```

文本：

```text
I love this movie
```

会转换为类似：

```text
[1, 1, 0, 1]
```

BoW 不保存单词顺序，只记录单词是否出现或出现次数。

## 5. 模型结构

模型结构为：

```text
Bag-of-Words 输入
→ Linear(vocab_size, 64)
→ ReLU
→ Dropout(0.2)
→ Linear(64, 2)
→ 两个类别 logits
```

输出的两个值分别对应：

```text
[消极类别分数, 积极类别分数]
```

训练时使用 `CrossEntropyLoss`，因此模型最后一层不额外添加 Softmax。

## 6. 环境安装

推荐使用 Python 3.10。

创建 Conda 环境：

```bash
conda create -n sentiment-repro python=3.10 -y
conda activate sentiment-repro
```

安装依赖：

```bash
pip install -r requirements.txt
```

## 7. 训练方法

在项目根目录运行：

```bash
python train.py
```

训练脚本将执行：

* 加载训练数据。
* 使用训练集建立词表。
* 创建 Dataset 和 DataLoader。
* 训练 MLP。
* 记录每个 epoch 的平均 loss 和训练准确率。
* 根据最低训练 loss 保存最佳 checkpoint。
* 保存训练 loss 曲线。

训练输出文件保存在：

```text
outputs/
```

主要文件：

```text
outputs/best_checkpoint.pth
outputs/loss_curve.png
```

## 8. 评估方法

训练完成后运行：

```bash
python eval.py
```

评估脚本将：

1. 加载 `outputs/best_checkpoint.pth`。
2. 恢复模型参数和训练词表。
3. 加载测试集。
4. 使用 checkpoint 中的训练词表转换测试文本。
5. 在 `model.eval()` 和 `torch.no_grad()` 环境下重新计算测试准确率。
6. 验证 checkpoint 重载前后的评估结果是否一致。

## 9. 实验结果

本次实验配置：

* 隐藏层维度：64
* Dropout：0.2
* 损失函数：CrossEntropyLoss
* 优化器：Adam
* 学习率：0.001
* Epoch 数量：200
* Batch size：按实际配置填写

最终结果：

* 最佳训练 loss：按实际结果填写
* 最终训练 accuracy：按实际结果填写
* 测试集 accuracy：按实际结果填写

训练 loss 曲线：

```text
outputs/loss_curve.png
```

## 10. 项目局限与后续改进

当前项目主要用于学习完整的文本分类训练流程，存在以下局限：

1. 数据集规模较小，测试准确率不能代表真实场景中的泛化能力。
2. 测试文本与训练文本可能具有较高相似度。
3. Bag-of-Words 不保存词序信息。
4. BoW 难以正确理解否定关系，例如 `not bad`。
5. 当前最佳 checkpoint 根据训练 loss 选择，更规范的做法是增加验证集，并根据验证集指标保存模型。
6. 后续可以尝试词嵌入、TextCNN、RNN 或 Transformer 等模型。

## 干净环境复现检查

在一个新环境中依次执行：

```bash
conda create -n sentiment-repro python=3.10 -y
conda activate sentiment-repro
pip install -r requirements.txt
python train.py
python eval.py
```

预期结果：

* 训练程序正常完成。
* `outputs/best_checkpoint.pth` 正常生成。
* `outputs/loss_curve.png` 正常生成。
* `eval.py` 能成功加载模型。
* 重载前后测试准确率一致。
