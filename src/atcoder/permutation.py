# %%
import itertools
import sys
from typing import Any, List

sys.setrecursionlimit(10 ** 6)


class Permutation:
    def permutations(self, nums: List[Any], r: int):
        self.nums = nums
        self.n = len(self.nums)
        self.r = r
        self.ret = []
        self.used = [False] * self.n
        self.perm = [0] * self.r
        self._dfs(0)
        return self.ret

    def _dfs(self, pos: int):
        if pos == self.r:
            self.ret.append(tuple(self.perm))
            return

        for i in range(self.n):
            if not self.used[i]:
                self.perm[pos] = self.nums[i]
                self.used[i] = True
                self._dfs(pos + 1)
                self.used[i] = False


if __name__ == "__main__":
    nums = [1, 2, 4, 10, 5]
    r = 3

    assert Permutation().permutations(nums, r) == list(itertools.permutations(nums, r))
    print(Permutation().permutations(nums, r))
    print()
    print(list(itertools.permutations(nums, r)))
