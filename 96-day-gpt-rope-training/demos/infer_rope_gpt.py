import tensorflow as tf
from model.gpt_rope import GPTRoPE
from loaders.dataset import GPTDataset

ds = GPTDataset("data/tiny.txt")

model = GPTRoPE(
    vocab_size=len(ds.vocab),
    d_model=64,
    num_heads=4,
    d_ff=128,
    num_layers=2
)

model.build((1,8))
model.load_weights("gpt_rope.h5")

x = tf.constant([[ds.word2id["hello"]]])
for _ in range(6):
    logits = model(x)
    next_id = tf.argmax(logits[:, -1, :], axis=-1)
    x = tf.concat([x, tf.expand_dims(next_id, 1)], axis=1)

print("Generated:", [ds.id2word[i] for i in x.numpy()[0]])
