# Simple Recall@K and Precision@K intuition

relevant_docs = {"refund policy"}
retrieved_docs = ["shipping policy", "refund policy", "company history"]

k = 2
top_k = retrieved_docs[:k]

true_positives = len(relevant_docs.intersection(top_k))

precision_at_k = true_positives / k
recall_at_k = true_positives / len(relevant_docs)

print("Top-K retrieved:", top_k)
print("Precision@K:", precision_at_k)
print("Recall@K:", recall_at_k)
