N, X = map(int, input().split())

X -= 1

tot = [0] * (N + 1)
patty = [0] * (N + 1)

tot[0] = 1
patty[0] = 1
for i in range(1, N + 1):
    tot[i] = tot[i - 1] * 2 + 3
    patty[i] = patty[i - 1] * 2 + 1


def solve(level, x):
    if level == 0:
        return 1

    if x < 1:
        return 0
    x -= 1

    if x < tot[level - 1]:
        return solve(level - 1, x)
    x -= tot[level - 1]

    if x < 1:
        return patty[level - 1] + 1
    x -= 1

    if x < tot[level - 1]:
        return patty[level - 1] + 1 + solve(level - 1, x)
    x -= tot[level - 1]

    return patty[level - 1] * 2 + 1


print(solve(N, X))
