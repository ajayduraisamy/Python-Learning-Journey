import tensorflow as tf
from tensorflow.keras import layers, models

def build_transfer_model():
    # Load VGG16 pretrained on ImageNet
    base = tf.keras.applications.VGG16(
        include_top=False,
        input_shape=(224,224,3),
        weights="imagenet"
    )

    # Freeze base layers
    base.trainable = False

    model = models.Sequential([
        base,
        layers.Flatten(),
        layers.Dense(128, activation="relu"),
        layers.Dropout(0.5),
        layers.Dense(10, activation="softmax")  # MNIST classes
    ])

    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model
