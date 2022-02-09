class UnionFind:
    def __init__(self, N):
        self.par = [i for i in range(N + 1)]

    def find(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if x < y:
            x, y = y, x
        self.par[x] = y

    def one_root(self):
        for i in range(1, len(self.par) - 1):
            if not self.same(i, i + 1):
                return False
        return True


N, M = map(int, input().split())
qs = [list(map(int, input().split())) for _ in range(M)]
uf = UnionFind(N)

ans = 0
for i in range(len(qs)):
    uf = UnionFind(N)
    for j, q in enumerate(qs):
        if i != j:
            uf.union(q[0], q[1])
    if not uf.one_root():
        ans += 1
print(ans)
