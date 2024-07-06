import tensorflow as tf
from tensorflow.keras import layers
from layers.mha_rope import MultiHeadAttentionRoPE

class GPTBlockRoPE(layers.Layer):
    def __init__(self, d_model, num_heads, d_ff):
        super().__init__()
        self.mha = MultiHeadAttentionRoPE(num_heads, d_model)
        self.ffn = tf.keras.Sequential([
            layers.Dense(d_ff, activation="relu"),
            layers.Dense(d_model)
        ])
        self.norm1 = layers.LayerNormalization(epsilon=1e-6)
        self.norm2 = layers.LayerNormalization(epsilon=1e-6)

    def call(self, x):
        attn = self.mha(x)
        x = self.norm1(x + attn)

        ffn_out = self.ffn(x)
        return self.norm2(x + ffn_out)
