import numpy as np

N, M = map(int, input().split())

A = list(map(int, input().split()))
C = list(map(int, input().split()))

polyA = np.poly1d(list(reversed(A)))
polyC = np.poly1d(list(reversed(C)))

polyB = polyC / polyA

coefB = list(map(int, polyB[0].c))

ans = list(reversed(coefB))
print(*ans)
