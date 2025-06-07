# Conceptual embedding quality comparison

queries = [
    "refund policy",
    "return product",
    "money back rules"
]

documents = [
    "Our refund policy allows returns within 30 days.",
    "Shipping information and delivery times."
]

print("Query-document similarity intuition:")
for q in queries:
    for d in documents:
        print(f"Query: '{q}' -> Doc: '{d[:30]}...'")
        #print(f"Similarity: {q[:30]}... -> {d[:30]}...: {similarity(q[:30], d[:30])}")