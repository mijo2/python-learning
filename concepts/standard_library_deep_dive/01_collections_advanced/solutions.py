# Collections Advanced Types Exercises Solutions

from collections import Counter, deque

words = ['apple', 'banana', 'apple', 'cherry']
counter = Counter(words)
print(counter.most_common(1))  # [('apple', 2)]

dq = deque()
dq.append(1)
dq.append(2)
print(dq.popleft())  # 1