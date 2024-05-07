# 10_real_pipeline_example.py
# Real-world generator pipeline: reading + filtering + transforming

def read_lines():
    for line in ["apple", "banana", "kiwi", "grape", "mango"]:
        yield line

def filter_short(lines):
    for line in lines:
        if len(line) <= 5:
            yield line

def to_upper(lines):
    for line in lines:
        yield line.upper()

result = to_upper(filter_short(read_lines()))
print(list(result))
