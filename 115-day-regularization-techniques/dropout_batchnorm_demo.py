import numpy as np

# Simulated activations
np.random.seed(42)
activations = np.random.randn(1000)

# Dropout
dropout_rate = 0.5
mask = np.random.binomial(1, 1 - dropout_rate, size=activations.shape)
dropout_output = activations * mask

# Batch Normalization
mean = activations.mean()
std = activations.std()
batchnorm_output = (activations - mean) / (std + 1e-8)

print("Original mean/std:", activations.mean(), activations.std())
print("After Dropout mean/std:", dropout_output.mean(), dropout_output.std())
print("After BatchNorm mean/std:", batchnorm_output.mean(), batchnorm_output.std())
