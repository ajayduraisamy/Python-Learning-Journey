# 02_custom_iterator.py
# Creating a custom iterator class

class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.value < self.limit:
            self.value += 1
            return self.value
        else:
            raise StopIteration

c = Counter(5)
for i in c:
    print(i)
