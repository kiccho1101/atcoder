N, T = map(int, input().split())
ts = list(map(int, input().split()))

ans = 0
diffs = [ts[i + 1] - ts[i] for i in range(N - 1)]
for diff in diffs:
    ans += min(diff, T)
ans += T

print(ans)
