# 07_generator_pipeline.py
# Generator pipeline to process data lazily

def numbers():
    for i in range(1, 11):
        yield i

def squares(nums):
    for n in nums:
        yield n * n

def evens(nums):
    for n in nums:
        if n % 2 == 0:
            yield n

pipeline = evens(squares(numbers()))
print(list(pipeline))
