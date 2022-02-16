from collections import defaultdict
from itertools import product

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]


def calc(hs):
    rows = 0
    for i in range(H):
        if hs[i] == 1:
            rows += 1

    counter = defaultdict(int)
    for i in range(W):
        nums = []
        for j in range(H):
            if hs[j] == 1:
                nums.append(A[j][i])

        if len(set(nums)) == 1:
            counter[nums[0]] += 1

    return max(counter.values()) * rows if len(counter) > 0 else 0


ans = 0
for hs in product([0, 1], repeat=H):
    ans = max(ans, calc(hs))

print(ans)
