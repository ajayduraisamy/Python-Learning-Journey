import tensorflow as tf

# Load images from folder structure
def load_custom_dataset(root_dir="dataset", img_size=(224,224), batch_size=32):

    train_ds = tf.keras.utils.image_dataset_from_directory(
        root_dir,
        validation_split=0.2,
        subset="training",
        seed=42,
        image_size=img_size,
        batch_size=batch_size
    )

    val_ds = tf.keras.utils.image_dataset_from_directory(
        root_dir,
        validation_split=0.2,
        subset="validation",
        seed=42,
        image_size=img_size,
        batch_size=batch_size
    )

    class_names = train_ds.class_names

    return train_ds, val_ds, class_names
