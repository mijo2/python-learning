# Collections Advanced Types Examples

from collections import namedtuple, deque, Counter, defaultdict

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

# deque
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.pop()
print(list(dq))

# Counter
c = Counter('hello world')
print(c.most_common(2))

# defaultdict
dd = defaultdict(int)
for char in 'hello':
    dd[char] += 1
print(dict(dd))