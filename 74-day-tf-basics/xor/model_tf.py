import tensorflow as tf
from tensorflow.keras import layers, models

def build_model():
    model = models.Sequential([
        layers.Dense(2, activation='sigmoid', input_shape=(2,)),
        layers.Dense(1, activation='sigmoid')
    ])
    return model
