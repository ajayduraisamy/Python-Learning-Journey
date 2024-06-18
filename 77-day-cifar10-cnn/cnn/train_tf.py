import tensorflow as tf
from cnn.data import load_cifar10
from cnn.model_tf import build_cnn

(X_train, y_train), (X_test, y_test) = load_cifar10()
model = build_cnn()

datagen = tf.keras.preprocessing.image.ImageDataGenerator(
    rotation_range=15,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True
)

datagen.fit(X_train)

checkpoint = tf.keras.callbacks.ModelCheckpoint(
    "best_cifar10_cnn.h5", save_best_only=True, monitor="val_accuracy"
)

history = model.fit(
    datagen.flow(X_train, y_train, batch_size=64),
    epochs=10,
    validation_data=(X_test, y_test),
    callbacks=[checkpoint]
)

print("Training complete. Best model saved as best_cifar10_cnn.h5")
