import itertools

N, M = map(int, input().split())

graph = [set() for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[x].add(y)
    graph[y].add(x)

ans = 0
for bit in itertools.product((0, 1), repeat=N):
    people = [i for i in range(N) if bit[i] == 1]
    flag = True
    for i in range(len(people) - 1):
        for j in range(i + 1, len(people)):
            if people[i] not in graph[people[j]]:
                flag = False
                break
    if flag:
        ans = max(ans, sum(bit))

print(ans)
