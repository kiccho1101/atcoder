A, B, C = map(int, input().split())

ans = "NO"
for i in range(1, 101):
    if (i * A) % B == C:
        ans = "YES"

print(ans)
