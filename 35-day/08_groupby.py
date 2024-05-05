# 08_groupby.py
# groupby example (requires sorted input for meaningful groups)

from itertools import groupby

data = [('fruit','apple'), ('fruit','banana'), ('veg','carrot'), ('fruit','orange'), ('veg','lettuce')]

# group by category (sort first if necessary)
data_sorted = sorted(data, key=lambda x: x[0])
for key, group in groupby(data_sorted, key=lambda x: x[0]):
    print("Group:", key, "->", [item for item in group])
