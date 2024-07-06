import tensorflow as tf
from model.gpt_rope import GPTRoPE

model = GPTRoPE(
    vocab_size=100,
    d_model=32,
    num_heads=4,
    d_ff=64,
    num_layers=2
)

x = tf.constant([[1, 5, 7, 3, 9]])
out = model(x)

print("Output shape:", out.shape)
