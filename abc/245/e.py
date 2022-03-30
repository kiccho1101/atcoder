# 疑似multiset:segtreeを用いた実装

#####segfunc#####
from pyparsing import QuotedString


def segfunc_min(x, y):
    return min(x, y)  # 最小値


def segfunc_max(x, y):
    return max(x, y)  # 最大値


#####単位元(ide_ele)#####
ide_ele_min = float("inf")  # 最小値
ide_ele_max = -float("inf")  # 最大値


class SegTree:
    """
    参考：https://qiita.com/takayg1/items/c811bd07c21923d7ec69
    init(init_val, segfunc, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(N)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    j番目の要素を取り出すとき->sgt.tree[sgt.num+j]
    """

    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


class QuasiMultiset:
    def __init__(self, N):
        self.N = N
        self.cnt = [0] * self.N
        self.sgt_min = SegTree([N - 1] * N, segfunc_min, ide_ele_min)
        self.sgt_max = SegTree([0] * N, segfunc_max, ide_ele_max)

    def add(self, x):
        if self.cnt[x] == 0:
            self.sgt_min.update(x, x)
            self.sgt_max.update(x, x)
        self.cnt[x] += 1

    def delete(self, x):
        """
        値がxの要素を一つ削除
        """
        self.cnt[x] -= 1
        if self.cnt[x] == 0:
            self.sgt_min.update(x, self.N - 1)
            self.sgt_max.update(x, 0)

    def popMin(self):
        mi = self.sgt_min.query(0, self.N)
        self.delete(mi)
        return mi

    def popMax(self):
        ma = self.sgt_max.query(0, self.N)
        self.delete(ma)
        return ma

    def searchMin(self):
        return self.sgt_min.query(0, self.N)

    def searchMax(self):
        return self.sgt_max.query(0, self.N)

    def lower_bound(self, x):
        """
        x未満で最大の数を返す
        """
        return self.sgt_max.query(0, x)

    def upper_bound(self, x):
        """
        x以上で最小の数を返す
        """
        return self.sgt_min.query(x, self.N)

    def contain(self, x):
        """
        xが存在するか->bool
        """
        return bool(self.cnt[x])


N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))


boxes = [(A[i], B[i]) for i in range(len(A))]
chocolates = [(C[i], D[i]) for i in range(len(C))]

boxes.sort(reverse=True)
chocolates.sort(reverse=True)

multiset = QuasiMultiset(N)

while chocolates:
    c, d = chocolates.pop(0)
    idx = 0
    while idx < len(A):
        a, b = boxes[idx]
        if a < c:
            break
        multiset.add(b)

    yoko_min = multiset.upper_bound(d)
    if isinstance(yoko_min, float):
        print("No")
        exit()
    multiset.delete(yoko_min)

print("Yes")
