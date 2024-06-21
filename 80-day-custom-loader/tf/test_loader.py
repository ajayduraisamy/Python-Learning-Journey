from tf.dataset import load_custom_dataset
from tf.pipeline import prepare_pipeline

train_ds, val_ds, classes = load_custom_dataset()
train_ds = prepare_pipeline(train_ds)
val_ds = prepare_pipeline(val_ds, shuffle=False)

print("Classes:", classes)
print("Train batch shape:", next(iter(train_ds))[0].shape)
