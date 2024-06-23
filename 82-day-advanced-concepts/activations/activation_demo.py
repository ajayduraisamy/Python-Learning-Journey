import tensorflow as tf

# Swish
swish = tf.nn.swish

# GELU
gelu = tf.nn.gelu

# Mish custom
def mish(x):
    return x * tf.math.tanh(tf.math.softplus(x))

x = tf.constant([-2.0, -1.0, 0.0, 1.0, 2.0])

print("Swish:", swish(x).numpy())
print("GELU:", gelu(x).numpy())
print("Mish:", mish(x).numpy())
