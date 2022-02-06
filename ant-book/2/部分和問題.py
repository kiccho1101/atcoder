# %%
from itertools import product
from typing import List

a = [1, 2, 4, 7]
k = 13


def bfs(i: int, s: int, a: List[int]):
    if i == len(a):
        return s == k

    # a[i]を使わない場合
    if bfs(i + 1, s, a):
        return True

    # a[i]を使う場合
    if bfs(i + 1, s + a[i], a):
        return True

    return False


if bfs(0, 0, a):
    print("Yes")
else:
    print("No")
