import tensorflow as tf
from model.gpt_lora import GPTLoRA

model = GPTLoRA(vocab_size=50, d_model=32)
model.build((1,3))
model.load_weights("lora_weights.h5")

out = model(tf.constant([[1,2,3]]))
print("Output:", tf.argmax(out, axis=-1).numpy())
