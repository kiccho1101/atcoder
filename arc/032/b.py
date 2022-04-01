# ARC 032 B
# https://atcoder.jp/contests/arc032/tasks/arc032_2

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

    def get_groups(self):
        return set(self.par)


N, M = map(int, input().split())
uf = UnionFind(N)
for _ in range(M):
    a, b = map(int, input().split())
    uf.union(a - 1, b - 1)

s = set()
for i in range(N):
    s.add(uf.find(i))

print(len(s) - 1)
