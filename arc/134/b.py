import heapq


N = int(input())

S = list(input())


def heappush(queue, idx, val):
    heapq.heappush(queue, (val, -idx))


def heappop(queue):
    val, idx = heapq.heappop(queue)
    return val, -idx


queue = []
for i, s in enumerate(S):
    heappush(queue, i, s)

left = 0
right = len(S)
while queue:
    val, idx = heappop(queue)
    if left <= idx and S[left] == S[idx]:
        left += 1
        heappush(queue, idx, val)
    elif left < idx < right and S[left] > S[idx]:
        S[left], S[idx] = S[idx], S[left]
        left += 1
        right = idx

print("".join(S))
