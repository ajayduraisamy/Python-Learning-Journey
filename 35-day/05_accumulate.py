# 05_accumulate.py
# accumulate example (running totals and custom func)

from itertools import accumulate
import operator

nums = [1, 2, 3, 4]

# running sum
print("Accumulate sum:", list(accumulate(nums)))

# running product using operator.mul
print("Accumulate product:", list(accumulate(nums, operator.mul)))

# custom function (max)
print("Accumulate max:", list(accumulate([3,1,4,2], max)))
