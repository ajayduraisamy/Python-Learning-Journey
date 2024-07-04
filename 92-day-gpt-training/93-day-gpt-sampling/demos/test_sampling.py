import tensorflow as tf
from model.gpt_mini import GPTMini
from loaders.dataset import GPTDataset
from utils.generate import generate_text

# load dataset for mapping
ds = GPTDataset("../92-day-gpt-training/data/tiny.txt")
vocab_size = len(ds.vocab)

# create model
model = GPTMini(
    vocab_size=vocab_size,
    d_model=64,
    num_heads=4,
    d_ff=128,
    num_layers=2,
    max_len=30
)
model.build((1,10))
model.load_weights("../92-day-gpt-training/gpt-mini.h5")

# starting word
start = tf.constant([[ds.word2id["hello"]]])

print("=== Temperature 0.7 ===")
print(generate_text(model, start, 10, temperature=0.7).numpy())

print("\n=== Top-K (k=3) ===")
print(generate_text(model, start, 10, top_k=3).numpy())

print("\n=== Top-P (p=0.9) ===")
print(generate_text(model, start, 10, top_p=0.9).numpy())
