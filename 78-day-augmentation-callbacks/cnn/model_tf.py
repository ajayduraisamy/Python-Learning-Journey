import tensorflow as tf
from tensorflow.keras import layers, models
from cnn.augment import get_aug_layers

def build_cnn():
    aug_layers = get_aug_layers()

    model = models.Sequential([
        layers.Input(shape=(28,28,1)),
        aug_layers,

        layers.Conv2D(32, 3, activation='relu'),
        layers.MaxPooling2D(),

        layers.Conv2D(64, 3, activation='relu'),
        layers.MaxPooling2D(),

        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(10, activation='softmax')
    ])

    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    return model
