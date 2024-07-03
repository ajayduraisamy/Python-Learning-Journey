import tensorflow as tf
from model.gpt_mini import GPTMini
from loaders.dataset import GPTDataset
from utils.generate import generate_text

ds = GPTDataset("data/tiny.txt")
vocab_size = len(ds.vocab)

model = GPTMini(
    vocab_size=vocab_size,
    d_model=64,
    num_heads=4,
    d_ff=128,
    num_layers=2,
    max_len=20
)

model.build((1,10))
model.load_weights("gpt-mini.h5")

start = tf.constant([[ds.word2id["hello"]]])
output = generate_text(model, start, max_new_tokens=10)

print("Generated IDs:", output.numpy())
print("Generated Words:", [ds.id2word[i] for i in output.numpy()[0]])
