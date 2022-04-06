# Union Find Tree
# https://www.slideshare.net/iwiwi/ss-3578491
# https://blog.hamayanhamayan.com/entry/2017/10/04/101826


class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.par = [-1] * n
        self.history = []

    def find(self, x: int) -> int:
        if self.par[x] < 0:
            return x
        return self.find(self.par[x])

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def undo(self):
        for _ in range(2):
            first, second = self.history.pop()
            self.par[first] = second

    def size(self, x: int):
        return -self.par[self.find(x)]

    def union(self, x: int, y: int) -> None:
        x = self.find(x)
        y = self.find(y)
        self.history.append((x, self.par[x]))
        self.history.append((y, self.par[x]))
        if x == y:
            return
        if self.par[x] > self.par[y]:
            x, y = y, x
        self.par[x] += self.par[y]
        self.par[y] = x
