N, M = map(int, input().split())

ans = 0
for i in range(1, M + 1):
    if i * i > M:
        break
    if M % i == 0:
        j = M // i
        if i >= N:
            ans = max(ans, j)
        if j >= N:
            ans = max(ans, i)

print(ans)
