import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Old-style augmentation (Keras)
def get_generator():
    return ImageDataGenerator(
        rotation_range=15,
        width_shift_range=0.1,
        height_shift_range=0.1,
        zoom_range=0.2
    )

# New-style augmentation (layers)
def get_aug_layers():
    return tf.keras.Sequential([
        tf.keras.layers.RandomRotation(0.1),
        tf.keras.layers.RandomTranslation(0.1, 0.1),
        tf.keras.layers.RandomZoom(0.1)
    ])
