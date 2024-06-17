import tensorflow as tf

def load_mnist():
    (X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

    # Normalize (0–255 → 0–1)
    X_train = X_train.astype("float32") / 255.0
    X_test = X_test.astype("float32") / 255.0

    # Add channel dimension
    X_train = X_train[..., tf.newaxis]
    X_test = X_test[..., tf.newaxis]

    return (X_train, y_train), (X_test, y_test)
