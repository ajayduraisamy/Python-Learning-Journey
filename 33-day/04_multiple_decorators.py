# 04_multiple_decorators.py
# Multiple decorators

def star(func):
    def wrapper():
        print("*" * 10)
        func()
        print("*" * 10)
    return wrapper

def hash_line(func):
    def wrapper():
        print("#" * 10)
        func()
        print("#" * 10)
    return wrapper

@star
@hash_line
def greet():
    print("Hello Ajay!")

greet()
