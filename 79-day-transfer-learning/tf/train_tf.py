import tensorflow as tf
from tf.data import load_dataset
from tf.model_tf import build_transfer_model

(X_train, y_train), (X_test, y_test) = load_dataset()

model = build_transfer_model()

checkpoint = tf.keras.callbacks.ModelCheckpoint(
    "best_vgg16_transfer.h5",
    save_best_only=True,
    monitor="val_accuracy"
)

history = model.fit(
    X_train, y_train,
    epochs=3,
    batch_size=32,
    validation_data=(X_test, y_test),
    callbacks=[checkpoint]
)

print("Training done. Best model saved as best_vgg16_transfer.h5")
