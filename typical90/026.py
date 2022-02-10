N = int(input())

graph = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

group = [[], []]
q = [[0, -1, 0]]
while q:
    v, past, color = q.pop()
    group[color].append(v + 1)
    for i in graph[v]:
        if i == past:
            continue
        q.append([i, v, color ^ 1])

if len(group[0]) >= N // 2:
    print(*group[0][: N // 2])
else:
    print(*group[1][: N // 2])
