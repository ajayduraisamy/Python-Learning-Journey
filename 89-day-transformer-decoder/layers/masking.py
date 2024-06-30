import tensorflow as tf

def create_look_ahead_mask(size):
    # Upper triangular matrix of 1s above diagonal
    mask = 1 - tf.linalg.band_part(tf.ones((size, size)), -1, 0)
    return mask  # 1 = masked, 0 = allowed
