# BIT (Binary Indexed Tree)
# https://qiita.com/R_olldIce/items/f2f7930e7f67963f0493
# https://www.slideshare.net/hcpc_hokudai/binary-indexed-tree


class BIT:
    def __init__(self, n: int):
        self.n = n
        self.data = [0.0] * n

    def add(self, p: int, x: float):
        p += 1  # 0-indexed -> 1-indexed
        while p <= self.n:
            self.data[p - 1] += x
            p += p & -p

    def _sum(self, idx: int) -> float:
        s = 0.0
        while idx > 0:
            s += self.data[idx - 1]
            idx -= idx & -idx
        return s

    def sum(self, left: int, right: int) -> float:
        return self._sum(right) - self._sum(left)


if __name__ == "__main__":

    def assertion(expected, actual):
        assert expected == actual, f"expected: {expected}, actual: {actual}"

    arr = [2, 3, 2, 4, 10]
    bit = BIT(8)
    for i, a in enumerate(arr):
        bit.add(i, a)

    assertion(bit.sum(0, 1), 2.0)
    assertion(bit.sum(1, 2), 3.0)
    assertion(bit.sum(1, 3), 5.0)
    assertion(bit.sum(0, 5), 21.0)
