import numpy as np

feature_map = np.random.randn(4, 4)

def max_pooling(x, size=2):
    out = np.zeros((x.shape[0] // size, x.shape[1] // size))
    for i in range(out.shape[0]):
        for j in range(out.shape[1]):
            region = x[i*size:(i+1)*size, j*size:(j+1)*size]
            out[i, j] = np.max(region)
    return out

print("Original shape:", feature_map.shape)
print("After pooling shape:", max_pooling(feature_map).shape)
