N, M = map(int, input().split())
graph = [0 for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if a > b:
        graph[a] += 1
    else:
        graph[b] += 1


ans = 0
for g in graph:
    if g == 1:
        ans += 1
print(ans)
