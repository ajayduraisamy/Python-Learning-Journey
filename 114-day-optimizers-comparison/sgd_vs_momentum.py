import numpy as np

# Loss: f(w) = (w - 4)^2
def grad(w):
    return 2 * (w - 4)

# SGD
w_sgd = 0.0
lr = 0.1

# Momentum
w_mom = 0.0
v = 0.0
beta = 0.9

print("Step | SGD | Momentum")

for step in range(15):
    # SGD update
    w_sgd -= lr * grad(w_sgd)

    # Momentum update
    v = beta * v + lr * grad(w_mom)
    w_mom -= v

    print(f"{step:>4} | {w_sgd:.4f} | {w_mom:.4f}")
