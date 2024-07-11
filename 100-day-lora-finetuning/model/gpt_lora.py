import tensorflow as tf
from tensorflow.keras import layers
from layers.lora_linear import LoRALinear

class GPTLoRA(tf.keras.Model):
    def __init__(self, vocab_size, d_model, rank=4):
        super().__init__()
        self.embed = layers.Embedding(vocab_size, d_model)
        self.lora = LoRALinear(vocab_size, rank)

    def call(self, x):
        x = self.embed(x)
        x = tf.reduce_mean(x, axis=1)
        return self.lora(x)
