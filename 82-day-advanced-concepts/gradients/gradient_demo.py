import tensorflow as tf

x = tf.Variable(1000.0)

with tf.GradientTape() as tape:
    y = x * x * x  # exploding gradient example

grad = tape.gradient(y, x)
print("Gradient:", grad.numpy())
