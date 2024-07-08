from tokenizer.bpe_tokenizer import BPETokenizer

tokenizer = BPETokenizer.load("tokenizer/merges.json")

text = "hello world"
tokens = tokenizer.encode(text)
decoded = tokenizer.decode(tokens)

print("Text:", text)
print("Tokens:", tokens)
print("Decoded:", decoded)
