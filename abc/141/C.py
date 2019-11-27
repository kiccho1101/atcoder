import numpy as np

Nn, Kk, Qq = input().split()
N, K, Q = int(Nn), int(Kk), int(Qq)
a = []
for q in range(Q):
    a.append(int(input()))
result = np.ones(N) * (K - Q)
for i in a:
    result[i - 1] += 1
result = result > 0
for r in result:
    if r:
        print("Yes")
    else:
        print("No")
