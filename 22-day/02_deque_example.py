# 02_deque_example.py
# Fast append/pop from both ends

from collections import deque

q = deque([1, 2, 3])
q.append(4)
q.appendleft(0)
q.pop()
q.popleft()

print("Deque:", q)
