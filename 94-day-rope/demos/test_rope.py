import tensorflow as tf
from layers.mha_rope import MultiHeadAttentionRoPE

mha = MultiHeadAttentionRoPE(num_heads=4, d_model=32)
x = tf.random.normal((1, 10, 32))

out = mha(x)
print("Output shape:", out.shape)
