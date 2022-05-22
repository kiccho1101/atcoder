N, M = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(M)]

is_friend = [[False] * (N + 1) for _ in range(N + 1)]

for a, b in ab:
    is_friend[a][b] = True
    is_friend[b][a] = True

for i in range(1, N + 1):
    friends = set()
    for j in range(1, N + 1):
        if is_friend[i][j]:
            for k in range(1, N + 1):
                if is_friend[j][k] and k != i and k != j and not is_friend[i][k]:
                    friends.add(k)
    print(len(friends))
