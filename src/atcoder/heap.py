# %%
from typing import Optional, Tuple


class Heap:
    def __init__(self):
        self.stack = []

    def add(self, x):
        print(f"Add {x} to heap")
        self.stack.append(x)
        self._shift_up()

    def pop(self) -> Optional[int]:
        if len(self.stack) == 0:
            return None
        if len(self.stack) == 1:
            ret = self.stack[0]
            self.stack = []
            return ret
        print("Pop root value")
        first = self.stack[0]
        last = self.stack.pop()
        self.stack[0] = last
        print("popped:", first)
        self._shift_down()
        return first

    def _shift_up(self):
        child_idx = len(self.stack) - 1
        parent_idx = self.get_parent_idx(child_idx)
        while parent_idx is not None:
            self.print()
            print("↓")
            if self.stack[parent_idx] > self.stack[child_idx]:
                self._swap(parent_idx, child_idx)
                child_idx = parent_idx
                parent_idx = self.get_parent_idx(child_idx)
            else:
                break
        self.print()

    def _shift_down(self):
        parent_idx = 0
        left_idx, right_idx = self.get_child_idx(parent_idx)
        while left_idx is not None:
            self.print()
            print("↓")
            if right_idx is None:
                if self.stack[parent_idx] > self.stack[left_idx]:
                    self._swap(parent_idx, left_idx)
                    parent_idx = left_idx
                    left_idx, right_idx = self.get_child_idx(parent_idx)
                else:
                    break
            else:
                if self.stack[left_idx] > self.stack[right_idx]:
                    left_idx = right_idx

                if self.stack[parent_idx] > self.stack[left_idx]:
                    self._swap(parent_idx, left_idx)
                    parent_idx = left_idx
                    left_idx, right_idx = self.get_child_idx(parent_idx)
                else:
                    break
        self.print()

    def get_parent_idx(self, k: int) -> Optional[int]:
        if k == 0:
            return None
        return (k - 1) // 2

    def get_child_idx(self, k: int) -> Tuple[Optional[int], Optional[int]]:
        left = 2 * k + 1
        right = 2 * k + 2
        if left >= len(self.stack):
            left = None
        if right >= len(self.stack):
            right = None
        return (left, right)

    def get_height(self) -> int:
        for i in range(100):
            if (1 << i) <= len(self.stack) < (1 << i + 1):
                return i + 1
        return -1

    def print(self):
        height = self.get_height()
        for i in range(100):
            start = pow(2, i) - 1
            end = pow(2, i + 1) - 1
            if start >= len(self.stack):
                break
            row = self.stack[start:end]
            print(" " * (height - i), *row)

    def _swap(self, idx1, idx2):
        self.stack[idx1], self.stack[idx2] = self.stack[idx2], self.stack[idx1]


heap = Heap()

heap.add(1)
heap.add(2)
heap.add(3)
heap.add(0)
heap.pop()
heap.add(2)
heap.add(2)
heap.add(10)
heap.add(-10)
heap.pop()

heap.print()
