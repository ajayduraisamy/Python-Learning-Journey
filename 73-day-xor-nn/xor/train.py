import numpy as np
from xor.data import load_xor
from xor.nn import NeuralNet

X, y = load_xor()
nn = NeuralNet(lr=0.5)

for epoch in range(5000):
    out = nn.forward(X)
    nn.backward(X, y)

    if epoch % 500 == 0:
        loss = np.mean((y - out)**2)
        print(f"Epoch {epoch}, Loss: {loss}")

print("\nFinal predictions:")
print(out.round())
