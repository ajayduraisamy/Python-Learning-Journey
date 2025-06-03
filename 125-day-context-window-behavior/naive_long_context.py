# Naive long-context prompt example

prompt = """
You will receive a long document.
Answer the question at the end.

[... imagine 10k tokens of content here ...]

Question:
What was the main decision mentioned at the beginning?
"""

print("Naive long-context prompt:")
print(prompt)
