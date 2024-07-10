import tensorflow as tf

def flash_attention(Q, K, V, block_size=32):
    """
    Q, K, V: (batch, seq_len, dim)
    """
    batch, seq_len, dim = Q.shape
    scale = tf.math.sqrt(tf.cast(dim, tf.float32))

    outputs = []

    for i in range(0, seq_len, block_size):
        Qi = Q[:, i:i+block_size, :]
        scores = tf.matmul(Qi, K, transpose_b=True) / scale
        weights = tf.nn.softmax(scores, axis=-1)
        out = tf.matmul(weights, V)
        outputs.append(out)

    return tf.concat(outputs, axis=1)
