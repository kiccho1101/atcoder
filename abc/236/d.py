import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())

A = [[0] * (2 * N + 1) for i in range(2 * N + 1)]

for i in range(1, 2 * N):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        A[i][j + (i + 1)] = tmp[j]
        A[j + (i + 1)][i] = tmp[j]

ans = 0

selected = [False] * (2 * N + 1)
pairs = []


def add(selected, pairs, i):
    selected[i] = True
    pairs.append(i)
    return selected, pairs


def remove(selected, pairs, i):
    selected[i] = False
    pairs.pop()
    return selected, pairs


def dfs(selected, pairs):
    global ans

    if len(pairs) == 2 * N:
        # スコアを計算して、最大値を更新する
        score = 0
        for i in range(0, 2 * N, 2):
            x = pairs[i]
            y = pairs[i + 1]
            score ^= A[x][y]
        ans = max(ans, score)

    elif len(pairs) % 2 == 0:
        # 偶数の場合、次の最小のダンサーを選ぶ
        i = 1
        while selected[i]:
            i += 1

        selected, pairs = add(selected, pairs, i)
        dfs(selected, pairs)
        selected, pairs = remove(selected, pairs, i)

    else:
        # 奇数の場合、残りのすべてのダンサーを選ぶ
        for i in range(1, 2 * N + 1):
            if not selected[i]:
                selected, pairs = add(selected, pairs, i)
                dfs(selected, pairs)
                selected, pairs = remove(selected, pairs, i)


dfs(selected, pairs)

print(ans)
