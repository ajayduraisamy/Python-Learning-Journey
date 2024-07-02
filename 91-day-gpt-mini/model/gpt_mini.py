import tensorflow as tf
from tensorflow.keras import layers
from layers.decoder_block import TransformerDecoderBlock
from layers.positional_encoding import positional_encoding

class GPTMini(tf.keras.Model):
    def __init__(self, vocab_size, d_model, num_heads, d_ff, num_layers, max_len=100):
        super().__init__()

        self.vocab_size = vocab_size
        self.d_model = d_model

        self.embedding = layers.Embedding(vocab_size, d_model)
        self.pos_encoding = positional_encoding(max_len, d_model)

        self.decoder_blocks = [
            TransformerDecoderBlock(d_model, num_heads, d_ff)
            for _ in range(num_layers)
        ]

        self.final_dense = layers.Dense(vocab_size)

    def call(self, x):
        seq_len = tf.shape(x)[1]

        x = self.embedding(x)
        x *= tf.math.sqrt(tf.cast(self.d_model, tf.float32))
        x += self.pos_encoding[:, :seq_len, :]

        for block in self.decoder_blocks:
            x = block(x, enc_output=x)  # GPT uses only masked attention

        logits = self.final_dense(x)
        return logits
