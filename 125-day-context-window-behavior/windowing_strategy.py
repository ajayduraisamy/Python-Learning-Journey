# Context windowing strategy (engineer approach)

sections = [
    "Section 1: Key decision overview",
    "Section 2: Supporting details",
    "Section 3: Edge cases",
    "Section 4: Final outcomes"
]

prompt = f"""
You are an analyst.

Summarize each section briefly.
Then answer: What is the key decision?

Sections:
{sections}
"""

print("Windowed / structured prompt:")
print(prompt)
