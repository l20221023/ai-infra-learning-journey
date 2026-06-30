from pathlib import Path

import torch
from torch.utils.data import DataLoader

from eval import evaluate
from src.dataset import SentimentDataset,load_sentiment_csv
from src.model import SentimentMLP


PROJECT_ROOT = Path(__file__).resolve().parent

TEST_DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "test.csv"
)

CHECKPOINT_PATH = (
    PROJECT_ROOT
    / "outputs"
    / "best_checkpoint.pth"
)


def main() -> None:
    checkpoint = torch.load(
        CHECKPOINT_PATH,
        map_location="cpu",
    )

    vocab = checkpoint["vocab"]

    test_texts, test_labels = load_sentiment_csv(
        TEST_DATA_PATH
    )

    test_dataset = SentimentDataset(test_texts,test_labels,vocab = vocab)

    test_loader = DataLoader(
        test_dataset,
        batch_size=2,
        shuffle=False,
    )

    model = SentimentMLP(
        input_dim=checkpoint["input_dim"],
        hidden_dim=checkpoint["hidden_dim"],
        output_dim=checkpoint["output_dim"],
        dropout=checkpoint.get(
            "dropout",
            0.2,
        ),
    )

    model.load_state_dict(
        checkpoint["model_state_dict"]
    )

    reloaded_accuracy = evaluate(
        model,
        test_loader,
    )

    saved_accuracy = checkpoint["test_accuracy"]

    print("模型加载成功")
    print("词表大小：", len(vocab))
    print(
        f"保存前测试准确率："
        f"{saved_accuracy:.4f}"
    )
    print(
        f"重载后测试准确率："
        f"{reloaded_accuracy:.4f}"
    )

    assert abs(
        saved_accuracy - reloaded_accuracy
    ) < 1e-8, "重载前后准确率不一致"

    print("Checkpoint 重载验证通过")


if __name__ == "__main__":
    main()