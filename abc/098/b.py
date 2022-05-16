N = int(input())
S = list(input())

ans = 0
for i in range(N):
    ans = max(ans, len(set(S[:i]).intersection(set(S[i:]))))

print(ans)
