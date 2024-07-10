import tensorflow as tf
import time
from layers.flash_attention import flash_attention

Q = tf.random.normal((1, 128, 64))
K = tf.random.normal((1, 128, 64))
V = tf.random.normal((1, 128, 64))

# Standard attention
start = time.time()
scores = tf.matmul(Q, K, transpose_b=True)
weights = tf.nn.softmax(scores, axis=-1)
out_std = tf.matmul(weights, V)
print("Standard attention time:", time.time() - start)

# Flash attention
start = time.time()
out_flash = flash_attention(Q, K, V, block_size=32)
print("Flash attention time:", time.time() - start)

print("Output shapes equal:", out_std.shape == out_flash.shape)
