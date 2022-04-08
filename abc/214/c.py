import heapq

N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

queue = []
for i in range(N):
    heapq.heappush(queue, (T[i], i))


dist = T.copy()
while queue:
    t, i = heapq.heappop(queue)
    nxt_i = (i + 1) % N
    if dist[nxt_i] > t + S[i]:
        dist[nxt_i] = t + S[i]
        heapq.heappush(queue, (t + S[i], nxt_i))

for i in range(N):
    print(dist[i])
