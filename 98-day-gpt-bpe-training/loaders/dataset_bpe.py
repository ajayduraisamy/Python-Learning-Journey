import tensorflow as tf
from tokenizer.bpe_loader import load_bpe

class GPTBPEdataset:
    def __init__(self, path, seq_len=12):
        tokenizer = load_bpe()
        text = open(path).read().strip()

        tokens = tokenizer.encode(text)
        self.vocab = sorted(set(tokens))
        self.token2id = {t:i for i,t in enumerate(self.vocab)}
        self.id2token = {i:t for t,i in self.token2id.items()}

        ids = [self.token2id[t] for t in tokens]
        self.data = []

        for i in range(len(ids) - seq_len):
            self.data.append((
                ids[i:i+seq_len],
                ids[i+1:i+seq_len+1]
            ))

    def tf_dataset(self, batch_size=4):
        x, y = zip(*self.data)
        return tf.data.Dataset.from_tensor_slices((x, y)).shuffle(100).batch(batch_size)
