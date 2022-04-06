def ind(y, x):
    return y * 10 + x


class UnionFind:
    def __init__(self, n=100):
        self.n = n
        self.par = [-1] * n
        self.history = []

    def find(self, idx):
        if self.par[idx] < 0:
            return idx
        return self.find(self.par[idx])

    def same(self, i, j):
        return self.find(i) == self.find(j)

    def undo(self):
        first, second = self.history.pop()
        self.par[first] = second
        first, second = self.history.pop()
        self.par[first] = second

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)
        self.history.append((i, self.par[i]))
        self.history.append((j, self.par[j]))
        if i == j:
            return
        if self.par[i] > self.par[j]:
            i, j = j, i
        self.par[i] += self.par[j]
        self.par[j] = i

    def group_num(self, field):
        parents = set()
        for y in range(10):
            for x in range(10):
                if field[y][x] == "o":
                    idx = ind(y, x)
                    parents.add(self.find(idx))
        return len(parents)


ds = [(0, 1), (1, 0), (-1, 0), (0, -1)]
field = [list(input()) for _ in range(10)]


def get_union_find(field):
    uf = UnionFind()
    for y in range(10):
        for x in range(10):
            if field[y][x] == "o":
                for dy, dx in ds:
                    ny = y + dy
                    nx = x + dx
                    if 0 <= ny < 10 and 0 <= nx < 10 and field[ny][nx] == "o":
                        uf.union(ind(y, x), ind(ny, nx))
    return uf


uf = get_union_find(field)
if uf.group_num(field) == 1:
    print("YES")
    exit()


for y in range(10):
    for x in range(10):
        if field[y][x] == "x":
            field[y][x] = "o"
            undo_count = 0
            for dy, dx in ds:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < 10 and 0 <= nx < 10 and field[ny][nx] == "o":
                    uf.union(ind(y, x), ind(ny, nx))
                    undo_count += 1
            if uf.group_num(field) == 1:
                print("YES")
                exit()
            field[y][x] = "x"
            for _ in range(undo_count):
                uf.undo()

print("NO")
