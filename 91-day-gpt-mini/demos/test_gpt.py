import tensorflow as tf
from model.gpt_mini import GPTMini
from utils.generate import generate_text

model = GPTMini(
    vocab_size=50,
    d_model=32,
    num_heads=4,
    d_ff=64,
    num_layers=2,
    max_len=30
)

start = tf.constant([[1, 5, 7]])  # fake tokenized prompt
output = generate_text(model, start, max_new_tokens=10)

print("Generated tokens:", output.numpy())
