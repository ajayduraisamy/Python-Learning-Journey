import tensorflow as tf
from layers.multihead_attention import MultiHeadAttention

mha = MultiHeadAttention(num_heads=2, d_model=4)

# Batch=1, SeqLen=3, Dim=4
Q = tf.constant([[[1., 0., 0., 0.],
                  [0., 1., 0., 0.],
                  [0., 0., 1., 0.]]])

K = tf.identity(Q)
V = tf.constant([[[10.0, 0.0, 0.0, 0.0],
                  [0.0, 20.0, 0.0, 0.0],
                  [0.0, 0.0, 30.0, 0.0]]])

out, weights = mha(Q, K, V)

print("Toy Attention Weights:\n", weights.numpy())
print("Toy Output:\n", out.numpy())
