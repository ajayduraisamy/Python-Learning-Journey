import tensorflow as tf
from model.gpt_rope import GPTRoPE
from loaders.dataset_bpe import GPTBPEdataset

ds = GPTBPEdataset("data/tiny.txt")

model = GPTRoPE(
    vocab_size=len(ds.vocab),
    d_model=64,
    num_heads=4,
    d_ff=128,
    num_layers=2
)

model.build((1,12))
model.load_weights("gpt_bpe.h5")

x = tf.constant([[0]])
for _ in range(8):
    logits = model(x)
    next_id = tf.argmax(logits[:, -1, :], axis=-1)
    x = tf.concat([x, tf.expand_dims(next_id, 1)], axis=1)

print("Generated token IDs:", x.numpy())
