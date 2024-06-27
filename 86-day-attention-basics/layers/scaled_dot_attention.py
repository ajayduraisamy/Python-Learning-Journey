import tensorflow as tf
from tensorflow.keras import layers

class ScaledDotProductAttention(layers.Layer):
    def __init__(self):
        super().__init__()

    def call(self, Q, K, V):
        # Calculate attention scores QKᵀ
        scores = tf.matmul(Q, K, transpose_b=True)

        # Scale by sqrt(d_k)
        d_k = tf.cast(tf.shape(K)[-1], tf.float32)
        scaled_scores = scores / tf.math.sqrt(d_k)

        # Softmax over last dimension
        weights = tf.nn.softmax(scaled_scores, axis=-1)

        # Weighted sum of values
        output = tf.matmul(weights, V)

        return output, weights
