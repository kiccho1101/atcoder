n, k = map(int, input().split())

A = [[0] * 5050 for _ in range(5050)]
for _ in range(n):
    a, b = map(int, input().split())
    A[a][b] += 1

for i in range(1, 5050):
    for j in range(5050):
        A[i][j] += A[i - 1][j]

for i in range(5050):
    for j in range(1, 5050):
        A[i][j] += A[i][j - 1]

ans = 0
for i in range(5001):
    for j in range(5001):
        max_i = min(5000, i + k + 1)
        max_j = min(5000, j + k + 1)
        ans = max(ans, A[max_i][max_j] + A[i][j] - A[max_i][j] - A[i][max_j])

print(ans)
