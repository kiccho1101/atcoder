from collections import deque


_ = int(input())

S = input()

q = deque([len(S)])
for j in range(len(S) - 1, -1, -1):
    if S[j] == "R":
        q.appendleft(j)
    else:
        q.append(j)
print(*q)
