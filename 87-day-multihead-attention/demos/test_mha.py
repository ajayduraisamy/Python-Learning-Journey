import tensorflow as tf
from layers.multihead_attention import MultiHeadAttention

mha = MultiHeadAttention(num_heads=4, d_model=32)

Q = tf.random.normal((1, 5, 32))  # (batch, seq_len, dim)
K = tf.random.normal((1, 5, 32))
V = tf.random.normal((1, 5, 32))

out, weights = mha(Q, K, V)

print("Output shape:", out.shape)
print("Attention weights shape:", weights.shape)
