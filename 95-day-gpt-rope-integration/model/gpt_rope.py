import tensorflow as tf
from tensorflow.keras import layers
from layers.gpt_block_rope import GPTBlockRoPE

class GPTRoPE(tf.keras.Model):
    def __init__(self, vocab_size, d_model, num_heads, d_ff, num_layers):
        super().__init__()
        self.embed = layers.Embedding(vocab_size, d_model)

        self.blocks = [
            GPTBlockRoPE(d_model, num_heads, d_ff)
            for _ in range(num_layers)
        ]

        self.norm = layers.LayerNormalization(epsilon=1e-6)
        self.lm_head = layers.Dense(vocab_size)

    def call(self, x):
        x = self.embed(x)

        for block in self.blocks:
            x = block(x)

        x = self.norm(x)
        return self.lm_head(x)
