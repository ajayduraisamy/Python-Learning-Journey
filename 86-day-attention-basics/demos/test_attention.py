import tensorflow as tf
from layers.scaled_dot_attention import ScaledDotProductAttention

att = ScaledDotProductAttention()

# Batch=1, SeqLen=4, Dim=8
Q = tf.random.normal((1,4,8))
K = tf.random.normal((1,4,8))
V = tf.random.normal((1,4,8))

out, weights = att(Q, K, V)

print("Output Shape:", out.shape)
print("Attention Weights:\n", weights.numpy())
