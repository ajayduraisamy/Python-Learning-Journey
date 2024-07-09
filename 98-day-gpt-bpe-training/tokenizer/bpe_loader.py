from tokenizer.bpe_tokenizer import BPETokenizer

def load_bpe():
    return BPETokenizer.load("../97-day-bpe-tokenizer/tokenizer/merges.json")
