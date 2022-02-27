N = int(input())
L = list(map(int, input().split()))

ans = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            a, b, c = L[i], L[j], L[k]
            if a == b or b == c or c == a:
                continue
            if abs(b - c) < a < b + c:
                ans += 1

print(ans)
