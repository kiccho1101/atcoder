MOD = 10 ** 9 + 7

N, K = map(int, input().split())
A = list(map(int, input().split()))


def cumsum(n):
    a = n % MOD
    b = (n + 1) % MOD
    return (a * b) // 2


A += A

ans = 0
for i in range(N):
    for j in range(i + 1, len(A)):
        if A[i] > A[j]:
            if j < N:
                ans += cumsum(K)
                ans %= MOD
            elif j - N < i:
                ans += cumsum(K - 1)
                ans %= MOD

print(ans)
