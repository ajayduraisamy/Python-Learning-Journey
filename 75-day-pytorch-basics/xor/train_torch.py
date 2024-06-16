import torch
import torch.nn as nn
import torch.optim as optim

from xor.data import load_xor
from xor.model_torch import XORNet

X, y = load_xor()

model = XORNet()
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.1)

for epoch in range(5000):
    optimizer.zero_grad()

    output = model(X)
    loss = criterion(output, y)

    loss.backward()
    optimizer.step()

    if epoch % 500 == 0:
        print(f"Epoch {epoch}, Loss {loss.item()}")

print("\nFinal predictions:")
print(model(X).round().detach())

torch.save(model.state_dict(), "xor_pytorch.pth")
print("Model saved as xor_pytorch.pth")
