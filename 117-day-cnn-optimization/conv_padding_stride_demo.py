import numpy as np

# Input feature map
input_map = np.random.randn(6, 6)
kernel = np.ones((3, 3))

def conv2d(input_map, kernel, stride=1, padding=0):
    if padding > 0:
        input_map = np.pad(input_map, padding)

    out_size = (input_map.shape[0] - kernel.shape[0]) // stride + 1
    output = np.zeros((out_size, out_size))

    for i in range(0, out_size):
        for j in range(0, out_size):
            region = input_map[
                i*stride:i*stride+kernel.shape[0],
                j*stride:j*stride+kernel.shape[1]
            ]
            output[i, j] = np.sum(region * kernel)

    return output

print("No padding, stride=1:", conv2d(input_map, kernel).shape)
print("Padding=1, stride=1:", conv2d(input_map, kernel, padding=1).shape)
print("Stride=2:", conv2d(input_map, kernel, stride=2).shape)
