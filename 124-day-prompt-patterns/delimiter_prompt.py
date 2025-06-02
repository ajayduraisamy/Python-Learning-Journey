# Delimiter-based prompt pattern

prompt = """
Summarize the text below in 3 bullet points.

TEXT:
"""
prompt += "```Machine learning models require careful evaluation to avoid misleading metrics.```"

print(prompt)
