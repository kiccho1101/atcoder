import collections

k = int(input())
queue = collections.deque([i for i in range(1, 10)])

x = -1
for _ in range(k):
    x = queue.popleft()
    if x % 10 != 0:
        queue.append(x * 10 + x % 10 - 1)
    queue.append(x * 10 + x % 10)
    if x % 10 != 9:
        queue.append(x * 10 + x % 10 + 1)

print(x)
