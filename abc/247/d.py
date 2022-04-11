import collections

queue = collections.deque()

Q = int(input())
qs = [list(map(int, input().split())) for _ in range(Q)]

for i in range(Q):
    if qs[i][0] == 1:
        _, x, c = qs[i]
        queue.append((x, c))
    if qs[i][0] == 2:
        _, target = qs[i]
        ans = 0
        cnt = 0
        while True:
            x, c = queue.popleft()
            cnt += c
            if cnt == target:
                ans += x * c
                break
            elif cnt > target:
                ans += x * (c - (cnt - target))
                queue.appendleft((x, cnt - target))
                break
            else:
                ans += x * c
        print(ans)
