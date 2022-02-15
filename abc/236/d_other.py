import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())

A = [[-1] * (2 * N + 1) for _ in range(2 * N)]
for i in range(2 * N - 1):
    a = list(map(int, input().split()))
    for j in range(len(a)):
        A[i + 1][i + j + 2] = a[j]

pairs = []
selected = [False] * (2 * N + 1)

ans = -1


def add(pairs, selected, i):
    pairs.append(i)
    selected[i] = True
    return pairs, selected


def remove(pairs, selected, i):
    pairs.pop()
    selected[i] = False
    return pairs, selected


def dfs(pairs, selected):
    global ans
    if len(pairs) == 2 * N:
        score = 0
        for i in range(0, 2 * N, 2):
            x = pairs[i + 1]
            y = pairs[i]
            score ^= A[y][x]
        ans = max(ans, score)

    elif len(pairs) % 2 == 0:
        i = 1
        while selected[i]:
            i += 1

        pairs, selected = add(pairs, selected, i)
        dfs(pairs, selected)
        pairs, selected = remove(pairs, selected, i)

    else:
        for i in range(1, 2 * N + 1):
            if not selected[i]:
                pairs, selected = add(pairs, selected, i)
                dfs(pairs, selected)
                pairs, selected = remove(pairs, selected, i)


dfs(pairs, selected)

print(ans)
