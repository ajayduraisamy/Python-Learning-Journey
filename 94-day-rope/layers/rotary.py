import tensorflow as tf
import numpy as np

def rotary_embedding(seq_len, dim):
    inv_freq = 1.0 / (10000 ** (tf.range(0, dim, 2) / dim))
    positions = tf.range(seq_len)
    sinusoid = tf.einsum("i,j->ij", positions, inv_freq)

    sin = tf.sin(sinusoid)
    cos = tf.cos(sinusoid)
    return sin, cos

def apply_rope(x, sin, cos):
    x1 = x[..., ::2]
    x2 = x[..., 1::2]

    x_rotated = tf.concat(
        [x1 * cos - x2 * sin, x1 * sin + x2 * cos],
        axis=-1
    )
    return x_rotated
