import tensorflow as tf

class GPTDataset:
    def __init__(self, path, seq_len=8):
        words = open(path).read().strip().split()

        self.vocab = sorted(set(words))
        self.word2id = {w:i for i,w in enumerate(self.vocab)}
        self.id2word = {i:w for w,i in self.word2id.items()}

        tokens = [self.word2id[w] for w in words]
        self.data = []

        for i in range(len(tokens) - seq_len):
            self.data.append((
                tokens[i:i+seq_len],
                tokens[i+1:i+seq_len+1]
            ))

    def tf_dataset(self, batch_size=4):
        x, y = zip(*self.data)
        return tf.data.Dataset.from_tensor_slices((x, y)).shuffle(100).batch(batch_size)
