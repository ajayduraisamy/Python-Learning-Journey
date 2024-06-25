import tensorflow as tf
from tensorflow.keras import layers

def mobilenet_block(x, filters, stride=1):
    # Depthwise convolution
    out = layers.DepthwiseConv2D(kernel_size=3, strides=stride, padding='same')(x)
    out = layers.BatchNormalization()(out)
    out = layers.ReLU()(out)

    # Pointwise convolution (1x1)
    out = layers.Conv2D(filters, kernel_size=1)(out)
    out = layers.BatchNormalization()(out)
    out = layers.ReLU()(out)

    return out
