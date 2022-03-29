import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

BC = [tuple(map(int, input().split())) for _ in range(M)]

A.sort()
BC.sort(key=lambda x: x[1])

idx = 0
while BC and idx < len(A):
    cnt, num = BC.pop()
    for j in range(cnt):
        nj = idx + j
        if nj < len(A) and A[nj] < num:
            A[nj] = num
        else:
            break
    idx += cnt

print(sum(A))
