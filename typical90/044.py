from collections import deque


N, Q = map(int, input().split())
A = deque()
for a in list(map(int, input().split())):
    A.append(a)

qs = [list(map(int, input().split())) for _ in range(Q)]
for [t, x, y] in qs:
    x -= 1
    y -= 1
    if t == 1:
        tmp = A[y]
        A[y] = A[x]
        A[x] = tmp
    if t == 2:
        A.appendleft(A.pop())
    if t == 3:
        print(A[x])
