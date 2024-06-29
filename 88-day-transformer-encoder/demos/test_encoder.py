import tensorflow as tf
from layers.encoder_block import TransformerEncoderBlock

encoder = TransformerEncoderBlock(d_model=32, num_heads=4, d_ff=64)

# Batch=1, SeqLen=5, Dim=32
x = tf.random.normal((1, 5, 32))

out = encoder(x)

print("Input Shape :", x.shape)
print("Output Shape:", out.shape)
