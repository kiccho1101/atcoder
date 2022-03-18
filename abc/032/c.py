N, K = map(int, input().split())

S = [int(input()) for _ in range(N)]

if 0 in S:
    exit(print(len(S)))

ans = 0
right = 0
mul = 1
for left in range(len(S)):
    while right < len(S) and S[right] * mul <= K:
        mul *= S[right]
        right += 1

    ans = max(ans, right - left)

    if right == left:
        right += 1
    else:
        mul /= S[left]

print(ans)
