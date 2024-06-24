import tensorflow as tf
from tensorflow.keras import layers, models
from blocks.residual_block import residual_block

def build_simple_resnet():
    inputs = layers.Input(shape=(32, 32, 3))

    x = layers.Conv2D(32, 3, padding='same')(inputs)
    x = layers.BatchNormalization()(x)
    x = layers.ReLU()(x)

    # Residual blocks
    x = residual_block(x, 32)
    x = residual_block(x, 32)

    x = layers.MaxPooling2D()(x)

    x = residual_block(x, 64, use_projection=True)
    x = residual_block(x, 64)

    x = layers.GlobalAveragePooling2D()(x)
    outputs = layers.Dense(10, activation='softmax')(x)

    model = models.Model(inputs, outputs)
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    return model
