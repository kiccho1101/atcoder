import heapq

K, T = map(int, input().split())

A = list(map(int, input().split()))

queue = []

for i, a in enumerate(A):
    heapq.heappush(queue, -a)

a = heapq.heappop(queue)
a = -a
last_a = a

ans = 0
while queue:
    a = heapq.heappop(queue)
    a = -a
    last_a -= 1
    if last_a > 0:
        heapq.heappush(queue, -last_a)
    last_a = a

print(last_a - 1)
