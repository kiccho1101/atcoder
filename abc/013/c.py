N, H = map(int, input().split())
A, B, C, D, E = map(int, input().split())

INF = 10 ** 18
ans = INF
for i in range(0, N + 1):
    j = max(0, (-H - i * B + E * N - E * i) // (D + E) + 1)
    cost = A * i + C * j
    ans = min(ans, cost)

print(ans)
