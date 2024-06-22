import tensorflow as tf
from tf.dataset import load_fruit_dataset
from tf.model_tf import build_model

train_ds, val_ds, classes = load_fruit_dataset()
num_classes = len(classes)

model = build_model(num_classes)

checkpoint = tf.keras.callbacks.ModelCheckpoint(
    "best_fruit_model.h5",
    save_best_only=True,
    monitor="val_accuracy"
)

history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=5,
    callbacks=[checkpoint]
)

print("Training completed! Best model saved as best_fruit_model.h5")
