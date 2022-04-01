# Union Find Tree
# https://www.slideshare.net/iwiwi/ss-3578491
# https://blog.hamayanhamayan.com/entry/2017/10/04/101826


from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.par = list(range(n + 1))

    def find(self, x: int) -> int:
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> None:
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if x < y:
            x, y = y, x
        self.par[x] = y
