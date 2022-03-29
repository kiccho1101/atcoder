import math

N = int(input())

ans = float("inf")
s = int(math.sqrt(N)) + 1
for i in range(s, 0, -1):
    if N % i == 0:
        ans = min(ans, max(len(str(i)), len(str(N // i))))

print(ans)
