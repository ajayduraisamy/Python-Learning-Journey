import tensorflow as tf

# Build tf.data optimized pipeline
def prepare_pipeline(ds, shuffle=True):
    
    AUTOTUNE = tf.data.AUTOTUNE

    if shuffle:
        ds = ds.shuffle(1000)

    ds = ds.prefetch(buffer_size=AUTOTUNE)

    return ds

# Normalization layer for images
def get_preprocessing_layer():
    return tf.keras.Sequential([
        tf.keras.layers.Rescaling(1./255)
    ])
