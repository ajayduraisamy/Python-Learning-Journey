import numpy as np

class NeuralNet:
    from xor.backprop import backward
    def __init__(self, input_dim=2, hidden_dim=2, output_dim=1, lr=0.1):
        # initialize weights
        self.W1 = np.random.randn(input_dim, hidden_dim)
        self.b1 = np.zeros((1, hidden_dim))

        self.W2 = np.random.randn(hidden_dim, output_dim)
        self.b2 = np.zeros((1, output_dim))

        self.lr = lr

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def forward(self, X):
        # hidden layer
        self.z1 = np.dot(X, self.W1) + self.b1
        self.h1 = self.sigmoid(self.z1)

        # output layer
        self.z2 = np.dot(self.h1, self.W2) + self.b2
        self.output = self.sigmoid(self.z2)

        return self.output
