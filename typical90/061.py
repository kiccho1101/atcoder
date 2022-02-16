from collections import deque


q = deque()

Q = int(input())
operations = [list(map(int, input().split())) for _ in range(Q)]

for t, x in operations:
    if t == 1:
        q.appendleft(x)
    if t == 2:
        q.append(x)
    if t == 3:
        print(q[x - 1])
