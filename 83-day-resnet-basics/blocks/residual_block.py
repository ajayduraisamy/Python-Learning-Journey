import tensorflow as tf
from tensorflow.keras import layers

def residual_block(x, filters, use_projection=False):
    shortcut = x

    # First conv
    out = layers.Conv2D(filters, 3, padding='same')(x)
    out = layers.BatchNormalization()(out)
    out = layers.ReLU()(out)

    # Second conv
    out = layers.Conv2D(filters, 3, padding='same')(out)
    out = layers.BatchNormalization()(out)

    # Projection shortcut if needed
    if use_projection:
        shortcut = layers.Conv2D(filters, 1)(shortcut)
        shortcut = layers.BatchNormalization()(shortcut)

    # Add skip connection
    out = layers.add([out, shortcut])
    out = layers.ReLU()(out)

    return out
