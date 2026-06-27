# Sentiment Classification with MLP and Bag-of-Words

# 基于 MLP 和 Bag-of-Words 的文本情感分类

## 项目简介

本项目使用 Bag-of-Words 将英文评论转换为固定长度向量，
并使用 PyTorch MLP 完成积极与消极二分类。

## 数据标签

- 0：消极
- 1：积极

## 模型结构

Bag-of-Words
→ Linear
→ ReLU
→ Linear
→ 两个类别 logits

## 项目结构

说明各文件用途。

## 运行方法

```bash
python main.py