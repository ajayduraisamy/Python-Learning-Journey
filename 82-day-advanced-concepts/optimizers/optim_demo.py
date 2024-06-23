import tensorflow as tf

model = tf.keras.Sequential([tf.keras.layers.Dense(1)])

opt_adamw = tf.keras.optimizers.AdamW(learning_rate=0.001, weight_decay=0.01)
opt_radam = tf.keras.optimizers.RMSprop()

print("AdamW and RMSProp optimizers ready.")
