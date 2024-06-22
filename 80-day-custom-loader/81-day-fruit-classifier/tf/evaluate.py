import tensorflow as tf
from tf.dataset import load_fruit_dataset

_, val_ds, classes = load_fruit_dataset()
model = tf.keras.models.load_model("best_fruit_model.h5")

loss, acc = model.evaluate(val_ds)
print("Validation Accuracy:", acc)
print("Classes:", classes)
