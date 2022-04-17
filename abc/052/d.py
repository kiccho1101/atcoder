N, A, B = map(int, input().split())
X = list(map(int, input().split()))

ans = 0
for i in range(len(X) - 1):
    dist = X[i + 1] - X[i]
    if A * dist < B:
        ans += A * dist
    else:
        ans += B

print(ans)
