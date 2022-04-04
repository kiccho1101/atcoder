N, K = map(int, input().split())

n = N // K
ans = n * n * n

if K % 2 == 0:
    m = N // (K // 2)
    m -= n
    ans += m * m * m

print(ans)
