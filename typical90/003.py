import collections


N = int(input())

graph = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)


def bfs(x):
    dist = [-1 for _ in range(N)]
    max_point = 0
    max_dist = 0

    queue = collections.deque([x])
    dist[x] = 0

    while len(queue) > 0:
        p = queue.popleft()
        d = dist[p] + 1
        for q in graph[p]:
            if dist[q] == -1:
                dist[q] = d
                queue.append(q)
                if max_dist < d:
                    max_dist = d
                    max_point = q
    return max_dist, max_point


_, first_max_point = bfs(0)
second_max_dist, _ = bfs(first_max_point)

ans = second_max_dist + 1
print(ans)
