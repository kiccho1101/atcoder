import heapq
from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))

counter = defaultdict(int)
for a in A:
    counter[a] += 1


def heappush_max(A, x):
    heapq.heappush(A, (-x[0], x[1]))


def heappop_max(A):
    x, y = heapq.heappop(A)
    return (-x, y)


queue = []
for num, cnt in counter.items():
    heappush_max(queue, (cnt, num))


eated = 0

# 3枚以上のカードは自分で処理する
while True:
    if len(queue) == 0:
        break
    cnt, num = heappop_max(queue)
    if cnt < 3:
        if cnt == 2:
            heappush_max(queue, (cnt, num))
        break

    after_cnt = 1 if cnt % 2 == 1 else 2
    eated += cnt - after_cnt
    cnt = after_cnt
    if cnt == 2:
        heappush_max(queue, (cnt, num))

# 2枚以上あるカードを処理する
while True:
    if len(queue) == 0:
        break
    cnt, num = heappop_max(queue)
    if cnt == 2:
        eated += 2
        if len(queue) == 0:
            break
        heappop_max(queue)
    if cnt == 1:
        break

print(max(0, N - eated))
