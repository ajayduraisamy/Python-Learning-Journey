import tensorflow as tf
from layers.flash_attention import flash_attention

Q = tf.random.normal((1, 64, 32))
K = tf.random.normal((1, 64, 32))
V = tf.random.normal((1, 64, 32))

out = flash_attention(Q, K, V, block_size=16)
print("FlashAttention output shape:", out.shape)
