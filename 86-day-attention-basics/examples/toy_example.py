import tensorflow as tf
from layers.scaled_dot_attention import ScaledDotProductAttention

att = ScaledDotProductAttention()

# Simple toy example for understanding
Q = tf.constant([[[1.0, 0.0]]])  # queries
K = tf.constant([[[1.0, 0.0], [0.0, 1.0]]])  # keys
V = tf.constant([[[10.0], [5.0]]])  # values

out, weights = att(Q, K, V)

print("Attention weights:", weights.numpy())
print("Output:", out.numpy())
