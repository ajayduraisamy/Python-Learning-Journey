import tensorflow as tf
from tensorflow.keras import layers
from layers.feed_forward import FeedForward
from layers.multihead_attention import MultiHeadAttention

class TransformerEncoderBlock(layers.Layer):
    def __init__(self, d_model, num_heads, d_ff):
        super().__init__()
        self.mha = MultiHeadAttention(num_heads, d_model)
        self.ffn = FeedForward(d_model, d_ff)

        self.norm1 = layers.LayerNormalization(epsilon=1e-6)
        self.norm2 = layers.LayerNormalization(epsilon=1e-6)

    def call(self, x):
        # Multi-head attention + residual
        attn_out, _ = self.mha(x, x, x)
        out1 = self.norm1(x + attn_out)

        # FFN + residual
        ffn_out = self.ffn(out1)
        out2 = self.norm2(out1 + ffn_out)

        return out2
