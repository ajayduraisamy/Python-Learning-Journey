import tensorflow as tf

xavier = tf.keras.initializers.GlorotUniform()
he_init = tf.keras.initializers.HeNormal()

w_xavier = xavier(shape=(3,3))
w_he = he_init(shape=(3,3))

print("Xavier Init:\n", w_xavier.numpy())
print("\nHe Init:\n", w_he.numpy())
