import tensorflow as tf

class GPTDataset:
    def __init__(self, path, seq_len=20):
        text = open(path, "r").read().strip().split()

        self.vocab = sorted(set(text))
        self.word2id = {w:i for i,w in enumerate(self.vocab)}
        self.id2word = {i:w for w,i in self.word2id.items()}

        tokens = [self.word2id[w] for w in text]

        self.seq_len = seq_len
        self.data = []

        for i in range(len(tokens) - seq_len - 1):
            x = tokens[i:i+seq_len]
            y = tokens[i+1:i+seq_len+1]
            self.data.append((x,y))

    def get_tf_dataset(self, batch_size=4):
        xs, ys = zip(*self.data)
        ds = tf.data.Dataset.from_tensor_slices((list(xs), list(ys)))
        ds = ds.shuffle(500).batch(batch_size)
        return ds
