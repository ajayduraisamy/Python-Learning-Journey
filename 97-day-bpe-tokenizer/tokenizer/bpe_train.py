from collections import Counter, defaultdict
import json

def get_pairs(word):
    return [(word[i], word[i+1]) for i in range(len(word)-1)]

def train_bpe(text, vocab_size=50):
    words = text.strip().split()
    corpus = [list(word) + ["</w>"] for word in words]

    vocab = Counter(tuple(word) for word in corpus)
    merges = []

    while len(vocab) < vocab_size:
        pairs = Counter()
        for word, freq in vocab.items():
            for pair in get_pairs(word):
                pairs[pair] += freq

        if not pairs:
            break

        best = pairs.most_common(1)[0][0]
        merges.append(best)

        new_vocab = {}
        for word, freq in vocab.items():
            new_word = []
            i = 0
            while i < len(word):
                if i < len(word)-1 and (word[i], word[i+1]) == best:
                    new_word.append(word[i] + word[i+1])
                    i += 2
                else:
                    new_word.append(word[i])
                    i += 1
            new_vocab[tuple(new_word)] = freq
        vocab = new_vocab

    return merges

if __name__ == "__main__":
    text = open("../96-day-gpt-rope-training/data/tiny.txt").read()
    merges = train_bpe(text)
    json.dump(merges, open("merges.json", "w"))
    print("Saved merges:", merges)
