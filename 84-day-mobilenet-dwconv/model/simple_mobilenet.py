import tensorflow as tf
from tensorflow.keras import layers, models
from blocks.mobilenet_block import mobilenet_block

def build_simple_mobilenet():
    inputs = layers.Input(shape=(32, 32, 3))

    # Initial conv
    x = layers.Conv2D(32, 3, padding='same', strides=1)(inputs)
    x = layers.BatchNormalization()(x)
    x = layers.ReLU()(x)

    # MobileNet blocks
    x = mobilenet_block(x, 32)
    x = mobilenet_block(x, 64, stride=2)
    x = mobilenet_block(x, 128, stride=2)

    # Classification head
    x = layers.GlobalAveragePooling2D()(x)
    outputs = layers.Dense(10, activation='softmax')(x)

    model = models.Model(inputs, outputs)

    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    return model
