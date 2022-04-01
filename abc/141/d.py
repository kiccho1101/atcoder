import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))

A = list(map(lambda x: x * (-1), A))

heapq.heapify(A)

while M:
    a = heapq.heappop(A)
    a = -(-a // 2)
    heapq.heappush(A, a)
    M -= 1

print(sum(A) * -1)
