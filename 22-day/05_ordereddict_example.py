# 05_ordereddict_example.py
# OrderedDict maintains order of insertion

from collections import OrderedDict

od = OrderedDict()
od["name"] = "Ajay"
od["age"] = 22
od["city"] = "Chennai"

print("OrderedDict:", od)

od.move_to_end("name")
print("After move_to_end:", od)
