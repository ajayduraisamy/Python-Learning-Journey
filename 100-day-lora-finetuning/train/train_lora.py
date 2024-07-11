import tensorflow as tf
from model.gpt_lora import GPTLoRA

x = tf.constant([[1,2,3],[2,3,4]])
y = tf.constant([5,6])

model = GPTLoRA(vocab_size=50, d_model=32, rank=4)

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
opt = tf.keras.optimizers.Adam(1e-3)

for epoch in range(20):
    with tf.GradientTape() as tape:
        logits = model(x)
        loss = loss_fn(y, logits)
    grads = tape.gradient(loss, model.trainable_variables)
    opt.apply_gradients(zip(grads, model.trainable_variables))
    print(f"Epoch {epoch+1} Loss:", loss.numpy())

model.save_weights("lora_weights.h5")
print("LoRA weights saved")
