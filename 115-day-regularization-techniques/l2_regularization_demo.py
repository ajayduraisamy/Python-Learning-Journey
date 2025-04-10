import numpy as np

# Simple linear regression with L2 regularization
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

w = 0.0
lr = 0.01
lambda_l2 = 0.1

def loss_grad(w):
    # gradient of MSE + L2 penalty
    grad_mse = -2 * np.mean(X * (y - w * X))
    grad_l2 = 2 * lambda_l2 * w
    return grad_mse + grad_l2

for step in range(50):
    w -= lr * loss_grad(w)

print("Learned weight with L2:", w)
