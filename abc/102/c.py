import math


N = int(input())
A = list(map(int, input().split()))

diff = [A[i] - (i + 1) for i in range(N)]

diff.sort()

mid = diff[N // 2] if N % 2 == 1 else (diff[N // 2 - 1] + diff[N // 2]) // 2

ans = sum([abs(d - mid) for d in diff])

print(ans)
