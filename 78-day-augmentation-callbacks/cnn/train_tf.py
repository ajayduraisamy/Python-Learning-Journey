import tensorflow as tf
from cnn.data import load_mnist
from cnn.model_tf import build_cnn
from cnn.augment import get_generator

(X_train, y_train), (X_test, y_test) = load_mnist()
model = build_cnn()

datagen = get_generator()
datagen.fit(X_train)

callbacks = [
    tf.keras.callbacks.EarlyStopping(
        monitor="val_loss",
        patience=3,
        restore_best_weights=True
    ),
    tf.keras.callbacks.ReduceLROnPlateau(
        monitor="val_loss",
        factor=0.5,
        patience=2
    ),
    tf.keras.callbacks.ModelCheckpoint(
        "best_augmented_model.h5",
        save_best_only=True,
        monitor="val_accuracy"
    ),
    tf.keras.callbacks.TensorBoard(log_dir="logs")
]

history = model.fit(
    datagen.flow(X_train, y_train, batch_size=64),
    validation_data=(X_test, y_test),
    epochs=10,
    callbacks=callbacks
)

print("Training complete! Best model saved as best_augmented_model.h5")
