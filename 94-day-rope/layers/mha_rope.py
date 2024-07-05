import tensorflow as tf
from tensorflow.keras import layers
from layers.rotary import rotary_embedding, apply_rope

class MultiHeadAttentionRoPE(layers.Layer):
    def __init__(self, num_heads, d_model):
        super().__init__()
        assert d_model % num_heads == 0

        self.num_heads = num_heads
        self.d_model = d_model
        self.depth = d_model // num_heads

        self.wq = layers.Dense(d_model)
        self.wk = layers.Dense(d_model)
        self.wv = layers.Dense(d_model)
        self.dense = layers.Dense(d_model)

    def split_heads(self, x):
        x = tf.reshape(x, (tf.shape(x)[0], -1, self.num_heads, self.depth))
        return tf.transpose(x, perm=[0,2,1,3])

    def call(self, x):
        Q = self.split_heads(self.wq(x))
        K = self.split_heads(self.wk(x))
        V = self.split_heads(self.wv(x))

        seq_len = tf.shape(x)[1]
        sin, cos = rotary_embedding(seq_len, self.depth)

        Q = apply_rope(Q, sin, cos)
        K = apply_rope(K, sin, cos)

        scores = tf.matmul(Q, K, transpose_b=True)
        scores /= tf.math.sqrt(tf.cast(self.depth, tf.float32))
        weights = tf.nn.softmax(scores, axis=-1)
        out = tf.matmul(weights, V)

        out = tf.transpose(out, perm=[0,2,1,3])
        out = tf.reshape(out, (tf.shape(out)[0], -1, self.d_model))
        return self.dense(out)
