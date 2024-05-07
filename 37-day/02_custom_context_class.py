# 02_custom_context_class.py
# Custom class-based context manager

class MyContext:
    def __enter__(self):
        print("Entering block")
        return "DATA READY"
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting block")
        return False  # don't suppress exceptions

with MyContext() as val:
    print("Inside:", val)
