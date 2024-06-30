import tensorflow as tf
from tensorflow.keras import layers
from layers.multihead_attention import MultiHeadAttention
from layers.masking import create_look_ahead_mask
from layers.feed_forward import FeedForward

class TransformerDecoderBlock(layers.Layer):
    def __init__(self, d_model, num_heads, d_ff):
        super().__init__()
        self.mha1 = MultiHeadAttention(num_heads, d_model)   # masked self-attention
        self.mha2 = MultiHeadAttention(num_heads, d_model)   # encoder-decoder attention

        self.ffn = FeedForward(d_model, d_ff)

        self.norm1 = layers.LayerNormalization(epsilon=1e-6)
        self.norm2 = layers.LayerNormalization(epsilon=1e-6)
        self.norm3 = layers.LayerNormalization(epsilon=1e-6)

    def call(self, x, enc_output):
        seq_len = tf.shape(x)[1]

        mask = create_look_ahead_mask(seq_len)

        # 1. Masked self-attention
        att1, _ = self.mha1(x, x, x)
        out1 = self.norm1(x + att1)

        # 2. Encoder-decoder attention
        att2, _ = self.mha2(out1, enc_output, enc_output)
        out2 = self.norm2(out1 + att2)

        # 3. Feed forward network
        ffn_out = self.ffn(out2)
        out3 = self.norm3(out2 + ffn_out)

        return out3
