import numpy as np

def backward(self, X, y):
    m = len(X)

    # Output layer error
    d_output = (self.output - y) * (self.output * (1 - self.output))

    # Hidden layer error
    d_hidden = np.dot(d_output, self.W2.T) * (self.h1 * (1 - self.h1))

    # Update weights
    self.W2 -= self.lr * np.dot(self.h1.T, d_output)
    self.b2 -= self.lr * np.sum(d_output, axis=0, keepdims=True)

    self.W1 -= self.lr * np.dot(X.T, d_hidden)
    self.b1 -= self.lr * np.sum(d_hidden, axis=0, keepdims=True)
