import tensorflow as tf
from tensorflow.keras import layers

class MultiHeadAttention(layers.Layer):
    def __init__(self, num_heads, d_model):
        super().__init__()
        assert d_model % num_heads == 0  # must divide evenly

        self.num_heads = num_heads
        self.d_model = d_model
        self.depth = d_model // num_heads

        # Linear layers for Q, K, V
        self.wq = layers.Dense(d_model)
        self.wk = layers.Dense(d_model)
        self.wv = layers.Dense(d_model)

        # Final linear projection
        self.dense = layers.Dense(d_model)

    def split_heads(self, x):
        # x: (batch, seq_len, d_model)
        x = tf.reshape(x, (tf.shape(x)[0], -1, self.num_heads, self.depth))
        return tf.transpose(x, perm=[0, 2, 1, 3])  # (batch, heads, seq_len, depth)

    def scaled_attention(self, Q, K, V):
        scores = tf.matmul(Q, K, transpose_b=True)
        d_k = tf.cast(tf.shape(K)[-1], tf.float32)
        scaled_scores = scores / tf.math.sqrt(d_k)
        weights = tf.nn.softmax(scaled_scores, axis=-1)
        output = tf.matmul(weights, V)
        return output, weights

    def call(self, Q, K, V):
        Q = self.wq(Q)
        K = self.wk(K)
        V = self.wv(V)

        # Split into heads
        Q = self.split_heads(Q)
        K = self.split_heads(K)
        V = self.split_heads(V)

        # Scaled dot-product attention per head
        attention_output, weights = self.scaled_attention(Q, K, V)

        # Combine heads
        attention_output = tf.transpose(attention_output, perm=[0, 2, 1, 3])
        concat = tf.reshape(attention_output, (tf.shape(attention_output)[0], -1, self.d_model))

        # Final linear projection
        output = self.dense(concat)

        return output, weights
