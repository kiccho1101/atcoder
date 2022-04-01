import sys

sys.setrecursionlimit(10 ** 6)


class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))

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
        for i in range(len(self.par) - 1):
            if self.find(i) != self.find(i + 1):
                return False
        return True


N, M = map(int, input().split())
qs = [list(map(int, input().split())) for _ in range(M)]

ans = 0
for i in range(len(qs)):
    uf = UnionFind(N)
    for j, [a, b] in enumerate(qs):
        a -= 1
        b -= 1
        if i != j:
            uf.union(a, b)
    if not uf.one_root():
        ans += 1
print(ans)
