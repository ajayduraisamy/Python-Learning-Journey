import tensorflow as tf

# root_dir example: fruit-dataset
def load_fruit_dataset(root_dir="fruit-dataset", img_size=(224,224), batch_size=32):

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
    AUTOTUNE = tf.data.AUTOTUNE

    # Optimize pipeline
    train_ds = train_ds.shuffle(1000).prefetch(AUTOTUNE)
    val_ds = val_ds.prefetch(AUTOTUNE)

    return train_ds, val_ds, class_names
