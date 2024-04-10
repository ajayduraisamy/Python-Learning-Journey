# 03_split_join.py
# split() and join()

sentence = "python is super easy"

words = sentence.split(" ")  # string -> list
print("Split words:", words)

joined = "-".join(words)     # list -> string
print("Joined:", joined)
