from bisect import bisect_left


N = int(input())
A = list(map(int, input().split()))


def LIS(x):
    dp = [0] * N
    now = [0]
    for i in range(N):
        j = bisect_left(now, x[i])
        dp[i] = j

        if j == len(now):
            now.append(x[i])
        else:
            now[j] = x[i]
    return dp


x = LIS(A)
y = LIS(A[::-1])


ans = 0
for i in range(N):
    ans = max(ans, x[i] + y[N - i - 1] - 1)

print(ans)
