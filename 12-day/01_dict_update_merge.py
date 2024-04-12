# 01_dict_update_merge.py
# update() and merging dictionaries

person = {"name": "Ajay", "age": 22}
extra = {"city": "Chennai", "skill": "Python"}

person.update(extra)
print("Updated dict:", person)

merged = {**person, **extra}
print("Merged dict:", merged)
