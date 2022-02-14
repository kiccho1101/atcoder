N = int(input())

a = list(map(int, input().split()))

a.sort()

upper = a[:]

for i in range(N - 2, -1, -1):
    upper[i] += upper[i + 1]

ans = 0
for i in range(N - 1):
    ans += upper[i + 1] - a[i] * (N - i - 1)

print(ans)
