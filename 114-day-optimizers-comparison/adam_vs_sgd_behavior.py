import numpy as np

# Simple loss
def grad(w):
    return 2 * (w - 4)

# SGD
w_sgd = 0.0
lr = 0.1

# Adam variables
w_adam = 0.0
m, v = 0.0, 0.0
beta1, beta2 = 0.9, 0.999
eps = 1e-8
lr_adam = 0.1

print("Step | SGD | Adam")

for t in range(1, 15):
    g = grad(w_adam)

    # Adam update
    m = beta1 * m + (1 - beta1) * g
    v = beta2 * v + (1 - beta2) * (g ** 2)
    m_hat = m / (1 - beta1 ** t)
    v_hat = v / (1 - beta2 ** t)
    w_adam -= lr_adam * m_hat / (np.sqrt(v_hat) + eps)

    # SGD update
    w_sgd -= lr * grad(w_sgd)

    print(f"{t:>4} | {w_sgd:.4f} | {w_adam:.4f}")
