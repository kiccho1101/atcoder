class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.sizes = [1] * (n + 1)

    def find(self, x):
        if x == self.par[x]:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def same(self, x, y):
        return self.par[x] == self.par[y]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if x < y:
            x, y = y, x
        self.par[x] = y
        self.sizes[y] += self.sizes[x]


N, M = map(int, input().split())
D = [0] + list(map(int, input().split()))

uf = UnionFind(N)
for _ in range(M):
    a, b = map(int, input().split())
    uf.unite(a, b)
    D[a] -= 1
    D[b] -= 1
