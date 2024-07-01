import tensorflow as tf
from layers.transformer_model import FullTransformer

model = FullTransformer(
    vocab_size=5000,
    d_model=32,
    num_heads=4,
    d_ff=64,
    num_layers=2,
    max_len=50
)

enc_input = tf.constant([[5, 10, 6, 3, 2]])
dec_input = tf.constant([[1, 4, 8, 2]])

output = model(enc_input, dec_input)

print("Output shape:", output.shape)
