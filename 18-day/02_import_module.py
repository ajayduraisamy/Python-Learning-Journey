# 02_import_module.py
# Importing custom module

import 18-day.01_create_module as cm  # INVALID IN PYTHON
# Correct import below

from importlib.machinery import SourceFileLoader
cm = SourceFileLoader("cm", "18-day/01_create_module.py").load_module()

print(cm.greet("Ajay"))
print("Square:", cm.square(6))
