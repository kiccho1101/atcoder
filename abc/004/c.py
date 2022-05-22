N = int(input())

A = list(range(1, 7))

if N >= 30:
    N %= 30

for i in range(N):
    a = i % 5
    b = i % 5 + 1
    A[a], A[b] = A[b], A[a]

print(*A, sep="")
