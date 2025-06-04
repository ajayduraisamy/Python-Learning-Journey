# Very simplified BPE-like splitting intuition

def fake_bpe(text):
    splits = []
    for word in text.split():
        if len(word) > 6:
            splits.extend([word[:4], word[4:]])
        else:
            splits.append(word)
    return splits

text = "tokenization effectiveness matters"
tokens = fake_bpe(text)

print("Text:", text)
print("Fake BPE tokens:", tokens)
print("Token count:", len(tokens))
