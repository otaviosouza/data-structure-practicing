from collections import deque

d = deque()
d.append(1)
d.appendleft(2)
d.append(3)
d.appendleft(4)

for i in d:
    print(i, end=' ')  # 4, 2, 1, 3

d.pop()
d.popleft()
d.remove(1)

for i in d:
    print(i, end=' ')  # 2
