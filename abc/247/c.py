import sys

sys.setrecursionlimit(10 ** 6)


def solve(n):
    if n == 1:
        return [1]
    return solve(n - 1) + [n] + solve(n - 1)


print(*solve(int(input())))
