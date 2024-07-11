import tensorflow as tf
from tensorflow.keras import layers

class LoRALinear(layers.Layer):
    def __init__(self, units, rank=4):
        super().__init__()
        self.units = units
        self.rank = rank

    def build(self, input_shape):
        self.W = self.add_weight(
            shape=(input_shape[-1], self.units),
            initializer="glorot_uniform",
            trainable=False
        )
        self.A = self.add_weight(
            shape=(input_shape[-1], self.rank),
            initializer="random_normal",
            trainable=True
        )
        self.B = self.add_weight(
            shape=(self.rank, self.units),
            initializer="zeros",
            trainable=True
        )

    def call(self, x):
        return x @ self.W + x @ self.A @ self.B
