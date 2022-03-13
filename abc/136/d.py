S = input()

memo = [0] * len(S)

move = pow(10, 100)

num = 0
for i in range(len(S) - 1, -1, -1):
    if S[i] == "L":
        num = 0
    else:
        num += 1
        memo[i] = num

num = 0
for i in range(len(S)):
    if S[i] == "R":
        num = 0
    else:
        num += 1
        memo[i] = num

ans = [0] * len(S)
for i in range(len(S)):
    if S[i] == "R":
        ans[i + memo[i] - (move - memo[i]) % 2] += 1
    if S[i] == "L":
        ans[i - memo[i] + (move - memo[i]) % 2] += 1

print(*ans)
