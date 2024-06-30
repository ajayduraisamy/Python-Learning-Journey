import tensorflow as tf
from layers.decoder_block import TransformerDecoderBlock

decoder = TransformerDecoderBlock(d_model=32, num_heads=4, d_ff=64)

# Fake sequence input (batch=1, seq_len=5, dim=32)
x = tf.random.normal((1, 5, 32))

# Fake encoder output (like from Day 88)
enc_out = tf.random.normal((1, 5, 32))

output = decoder(x, enc_out)

print("Decoder output shape:", output.shape)
