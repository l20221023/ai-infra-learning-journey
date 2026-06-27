import torch

def evaluate(model,data_loader):
    model.eval()

    correct_count = 0
    sample_count = 0

    with torch.no_grad():
        for batch_x,batch_y in data_loader:
            logits = model(batch_x)

            predictions = torch.argmax(logits, dim=1)

            correct_count += (predictions == batch_y).sum().item()
            sample_count += batch_y.size(0)
        
        accuracy = correct_count / sample_count
        return accuracy