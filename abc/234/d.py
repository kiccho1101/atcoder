import heapq

N, K = map(int, input().split())
P = list(map(int, input().split()))

q = P[0:K]
print(min(q))
heapq.heapify(q)
for i in range(K, N):
    minim = heapq.heappop(q)
    minim = max(minim, P[i])
    heapq.heappush(q, minim)
    ans = heapq.heappop(q)
    print(ans)
    heapq.heappush(q, ans)
