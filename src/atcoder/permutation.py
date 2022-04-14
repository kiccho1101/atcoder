# %%
import itertools
import sys
from typing import Any, List

sys.setrecursionlimit(10 ** 6)


class Permutation:
    def permutations(self, nums: List[Any], n: int):
        self.nums = nums
        self.n = n
        self.ret = []
        self.used = [False] * (len(nums) + 1)
        self.perm = [0] * n
        self._dfs(0)
        return self.ret

    def _dfs(self, pos: int):
        if pos == self.n:
            self.ret.append(tuple(self.nums[i] for i in self.perm))
            return

        for i in range(len(self.nums)):
            if not self.used[i]:
                self.perm[pos] = i
                self.used[i] = True
                self._dfs(pos + 1)
                self.used[i] = False


if __name__ == "__main__":
    nums = [1, 2, 4, 10, 5]
    n = 3

    assert Permutation().permutations(nums, n) == list(itertools.permutations(nums, n))
    print(Permutation().permutations(nums, n))
    print()
    print(list(itertools.permutations(nums, n)))
