# PyTorch XOR Explanation

### Model:
- 2 input neurons
- 2 hidden neurons (sigmoid)
- 1 output neuron (sigmoid)

### Why XOR?
XOR is not linearly separable.
A neural network must learn non-linear representations.

### Why Sigmoid?
To match XOR output (0 or 1).

### Loss:
BCELoss for binary output.

### Optimizer:
Adam helps faster convergence.
