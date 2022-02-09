N, Q = map(int, input().split())
qs = [list(map(int, input().split())) for _ in range(Q)]


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


union_find = UnionFind(N)
for q in qs:
    if q[0] == 0:
        union_find.union(q[1], q[2])
    elif q[0] == 1:
        if union_find.same(q[1], q[2]):
            print("Yes")
        else:
            print("No")
