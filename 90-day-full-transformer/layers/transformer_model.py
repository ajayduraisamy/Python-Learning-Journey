import tensorflow as tf
from tensorflow.keras import layers
from layers.positional_encoding import positional_encoding
from layers.encoder_block import TransformerEncoderBlock
from layers.decoder_block import TransformerDecoderBlock

class FullTransformer(tf.keras.Model):
    def __init__(self, vocab_size, d_model, num_heads, d_ff, num_layers, max_len=100):
        super().__init__()

        self.d_model = d_model
        self.embedding = layers.Embedding(vocab_size, d_model)
        self.pos_encoding = positional_encoding(max_len, d_model)

        # encoder blocks
        self.encoder_layers = [
            TransformerEncoderBlock(d_model, num_heads, d_ff)
            for _ in range(num_layers)
        ]

        # decoder blocks
        self.decoder_layers = [
            TransformerDecoderBlock(d_model, num_heads, d_ff)
            for _ in range(num_layers)
        ]

        self.final_dense = layers.Dense(vocab_size)

    def call(self, enc_input, dec_input):
        seq_len = tf.shape(enc_input)[1]

        enc_x = self.embedding(enc_input)
        enc_x += self.pos_encoding[:, :seq_len, :]

        for layer in self.encoder_layers:
            enc_x = layer(enc_x)

        dec_x = self.embedding(dec_input)
        dec_x += self.pos_encoding[:, :tf.shape(dec_input)[1], :]

        for layer in self.decoder_layers:
            dec_x = layer(dec_x, enc_x)

        output = self.final_dense(dec_x)
        return output
