# Naive retrieval validation (WRONG)

retrieved_docs = [
    "Shipping policy details",
    "Company history overview",
    "Refund policy terms"
]

print("Retrieved docs:")
for d in retrieved_docs:
    print("-", d)

print("\nAssumption: If answer looks OK, retrieval is OK (WRONG)")
