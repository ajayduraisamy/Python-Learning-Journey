# 05_magic_methods.py
# Magic / dunder methods (__str__, __len__)

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}"

    def __len__(self):
        return self.pages

b = Book("Python Mastery", 350)
print(str(b))
print("Pages:", len(b))
