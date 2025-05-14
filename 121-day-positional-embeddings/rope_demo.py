import numpy as np

def rotate_half(x):
    x1, x2 = x[..., ::2], x[..., 1::2]
    return np.stack((-x2, x1), axis=-1).reshape(x.shape)

def apply_rope(x, pos):
    dim = x.shape[-1]
    theta = 1.0 / (10000 ** (np.arange(0, dim, 2) / dim))
    angle = pos * theta
    sin, cos = np.sin(angle), np.cos(angle)

    x_rot = rotate_half(x)
    x[..., ::2] = x[..., ::2] * cos - x_rot[..., ::2] * sin
    x[..., 1::2] = x[..., 1::2] * cos + x_rot[..., 1::2] * sin
    return x

# Example token embedding
x = np.random.randn(1, 6)
out = apply_rope(x.copy(), pos=3)

print("Original:", x)
print("After RoPE:", out)
