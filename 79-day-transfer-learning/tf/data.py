import tensorflow as tf

def load_dataset():
    # Load MNIST (28x28x1)
    (X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

    # Resize to VGG16 input size and convert grayscale → RGB
    X_train = tf.image.resize(tf.expand_dims(X_train, -1), (224,224))
    X_test = tf.image.resize(tf.expand_dims(X_test, -1), (224,224))

    X_train = tf.image.grayscale_to_rgb(X_train) / 255.0
    X_test = tf.image.grayscale_to_rgb(X_test) / 255.0

    return (X_train, y_train), (X_test, y_test)

    
