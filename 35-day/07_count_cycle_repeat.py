# 07_count_cycle_repeat.py
# infinite iterators: count, cycle, repeat (use with care)

from itertools import count, cycle, repeat
import itertools

# count: infinite counter starting from 10
counter = count(10)
print(next(counter), next(counter), next(counter))

# cycle: repeat elements of an iterable endlessly (show first 6)
cycler = cycle([1,2,3])
print([next(cycler) for _ in range(6)])

# repeat: repeat a single value many times (or n times if specified)
print("repeat 5 three times:", list(repeat(5, 3)))
