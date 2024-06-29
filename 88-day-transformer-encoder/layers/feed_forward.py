import tensorflow as tf
from tensorflow.keras import layers

class FeedForward(layers.Layer):
    def __init__(self, d_model, d_ff):
        super().__init__()
        self.dense1 = layers.Dense(d_ff, activation='relu')
        self.dense2 = layers.Dense(d_model)

    def call(self, x):
        x = self.dense1(x)
        x = self.dense2(x)
        return x
