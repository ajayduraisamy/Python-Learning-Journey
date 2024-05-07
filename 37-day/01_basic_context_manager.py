# 01_basic_context_manager.py
# Basic "with" usage

with open("sample.txt", "w") as f:
    f.write("Hello from context manager!")

print("File written successfully.")
