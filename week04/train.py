from pathlib import Path

import matplotlib.pyplot as plt
import torch
from torch import nn
from torch.utils.data import DataLoader

from eval import evaluate
from src.dataset import SentimentDataset,load_sentiment_csv
from src.model import SentimentMLP


PROJECT_ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = PROJECT_ROOT / "outputs"

DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "outputs"

TRAIN_DATA_PATH = DATA_DIR / "train.csv"
TEST_DATA_PATH = DATA_DIR / "test.csv"

CHECKPOINT_PATH = OUTPUT_DIR / "best_checkpoint.pth"
LOSS_CURVE_PATH = OUTPUT_DIR / "loss_curve.png"

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


def main() -> None:
    torch.manual_seed(42)

    train_texts, train_labels = load_sentiment_csv(
        TRAIN_DATA_PATH
    )

    test_texts, test_labels = load_sentiment_csv(
        TEST_DATA_PATH
    )

    # 只使用训练集建立 vocab
    train_dataset = SentimentDataset(
        train_texts,
        train_labels,
    )

    # 测试集复用训练集 vocab
    test_dataset = SentimentDataset(
        test_texts,
        test_labels,
        vocab=train_dataset.vocab,
    )

    train_loader = DataLoader(
        train_dataset,
        batch_size=4,
        shuffle=True,
    )

    test_loader = DataLoader(
        test_dataset,
        batch_size=2,
        shuffle=False,
    )

    input_dim = len(train_dataset.vocab)
    hidden_dim = 64
    output_dim = 2
    dropout = 0.2

    model = SentimentMLP(
        input_dim=input_dim,
        hidden_dim=hidden_dim,
        output_dim=output_dim,
        dropout=dropout,
    )

    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=0.001,
    )

    criterion = nn.CrossEntropyLoss()

    num_epochs = 200
    best_train_loss = float("inf")

    loss_history = []
    accuracy_history = []

    for epoch in range(num_epochs):
        model.train()

        total_loss = 0.0
        correct_count = 0
        sample_count = 0

        for batch_x, batch_y in train_loader:
            optimizer.zero_grad()

            logits = model(batch_x)
            loss = criterion(logits, batch_y)

            loss.backward()
            optimizer.step()

            current_batch_size = batch_y.size(0)

            total_loss += (
                loss.item() * current_batch_size
            )

            sample_count += current_batch_size

            predictions = torch.argmax(
                logits,
                dim=1,
            )

            correct_count += (
                predictions == batch_y
            ).sum().item()

        average_loss = total_loss / sample_count
        epoch_accuracy = correct_count / sample_count

        loss_history.append(average_loss)
        accuracy_history.append(epoch_accuracy)

        if epoch == 0 or (epoch + 1) % 50 == 0:
            print(
                f"Epoch [{epoch + 1}/{num_epochs}], "
                f"Loss: {average_loss:.4f}, "
                f"Accuracy: {epoch_accuracy:.4f}"
            )

        if average_loss < best_train_loss:
            best_train_loss = average_loss

            checkpoint = {
                "epoch": epoch + 1,
                "model_state_dict": model.state_dict(),
                "optimizer_state_dict": optimizer.state_dict(),
                "vocab": train_dataset.vocab,
                "input_dim": input_dim,
                "hidden_dim": hidden_dim,
                "output_dim": output_dim,
                "dropout": dropout,
                "best_train_loss": best_train_loss,
                "loss_history": loss_history.copy(),
                "accuracy_history": accuracy_history.copy(),
            }

            torch.save(
                checkpoint,
                CHECKPOINT_PATH,
            )

    # 加载最低训练 loss 对应的模型
    best_checkpoint = torch.load(
        CHECKPOINT_PATH,
        map_location="cpu",
    )

    model.load_state_dict(
        best_checkpoint["model_state_dict"]
    )

    test_accuracy = evaluate(
        model,
        test_loader,
    )

    print(
        f"最佳 Epoch：{best_checkpoint['epoch']}"
    )
    print(
        f"最佳训练 Loss："
        f"{best_checkpoint['best_train_loss']:.4f}"
    )
    print(
        f"测试集 Accuracy：{test_accuracy:.4f}"
    )

    # 将最佳模型的测试结果保存进 checkpoint
    best_checkpoint["test_accuracy"] = test_accuracy

    torch.save(
        best_checkpoint,
        CHECKPOINT_PATH,
    )

    plt.figure()

    plt.plot(
        range(1, len(loss_history) + 1),
        loss_history,
    )

    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title("Training Loss Curve")
    plt.tight_layout()

    plt.savefig(
        LOSS_CURVE_PATH,
        dpi=150,
        bbox_inches="tight",
    )

    plt.close()

    print(f"最佳模型已保存到：{CHECKPOINT_PATH}")
    print(f"Loss 曲线已保存到：{LOSS_CURVE_PATH}")


if __name__ == "__main__":
    main()