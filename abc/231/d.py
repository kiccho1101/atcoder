import collections


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [-1] * n

    def find(self, x):
        if self.par[x] < 0:
            return x
        return self.find(self.par[x])

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.par[x] > self.par[y]:
            x, y = y, x
        self.par[x] += self.par[y]
        self.par[y] = x


N, M = map(int, input().split())
uf = UnionFind(N)
neighbors = collections.defaultdict(set)

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    neighbors[a].add(b)
    neighbors[b].add(a)
    if uf.same(a, b) or len(neighbors[a]) > 2 or len(neighbors[b]) > 2:
        print("No")
        exit()

    uf.union(a, b)

print("Yes")
