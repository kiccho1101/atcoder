import itertools

n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    a = int(input())
    for _ in range(a):
        x, y = map(int, input().split())
        x -= 1
        graph[i].append((x, y))


def ok(bit, n, graph):
    for i, b in enumerate(bit):
        if b == 1:
            for x, y in graph[i]:
                if bit[x] != y:
                    return False
    return True


ans = 0
for bit in itertools.product((0, 1), repeat=n):
    if ok(bit, n, graph):
        ans = max(ans, sum(bit))

print(ans)
