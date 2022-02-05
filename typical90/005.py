from collections import deque


N, K = map(int, input().split())

S = input()

q = deque()
ans = ""

for i, s in enumerate(S):
    while q and q[-1] > s:
        q.pop()
    q.append(s)

    if N - K <= i:
        ans += q.popleft()

print(ans)
