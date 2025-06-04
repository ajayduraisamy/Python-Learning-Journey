# Naive assumption: words == tokens (WRONG)

sentences = [
    "Machine learning is powerful",
    "tokenization-effectiveness matters!",
    "email@example.com is one token?"
]

for s in sentences:
    words = s.split()
    print(f"Sentence: {s}")
    print(f"Word count: {len(words)}\n")
