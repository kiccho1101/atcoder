class UnionFind:
    def __init__(self, n: int):
        self.par = list(range(n + 1))

    def find(self, x: int):
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def same(self, x: int, y: int):
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if x < y:
            x, y = y, x
        self.par[x] = y


N, Q = map(int, input().split())
qs = [list(map(int, input().split())) for _ in range(Q)]

uf = UnionFind(N)
for p, a, b in qs:
    if p == 0:
        uf.union(a, b)
    if p == 1:
        if uf.same(a, b):
            print("Yes")
        else:
            print("No")
