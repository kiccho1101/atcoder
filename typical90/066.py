N = int(input())
L, R = [0] * N, [0] * N
for i in range(N):
    L[i], R[i] = map(int, input().split())

ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        x = R[i] - L[i] + 1
        y = R[j] - L[j] + 1
        under = x * y
        for k in range(L[i], R[i] + 1):
            top = max(0, min(k - 1, R[j]) - L[j] + 1)
            ans += top / under

print(ans)
