N, K = map(int, input().split())
R = sorted(list(map(int, input().split())), reverse=True)

ans = 0
for i in range(K):
    ans = (ans + R[K - i - 1]) / 2

print(ans)
