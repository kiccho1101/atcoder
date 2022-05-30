from collections import defaultdict
import heapq


Q = int(input())

min_heap = []
max_heap = []

nums_cnt = defaultdict(int)
nums_set = set()

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        x = q[1]
        nums_cnt[x] += 1
        if x not in nums_set:
            nums_set.add(x)
            heapq.heappush(min_heap, x)
            heapq.heappush(max_heap, -x)

    elif q[0] == 2:
        x, c = q[1:]
        del_count = min(c, nums_cnt[x])
        nums_cnt[x] -= del_count
        if nums_cnt[x] == 0 and x in nums_set:
            nums_set.remove(x)

    else:
        while min_heap[0] not in nums_set:
            heapq.heappop(min_heap)
        while -max_heap[0] not in nums_set:
            heapq.heappop(max_heap)
        print(-max_heap[0] - min_heap[0])
