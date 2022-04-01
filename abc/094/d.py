import math


N = int(input())
A = list(map(int, input().split()))

A.sort()


def combinations(p, r):
    return math.factorial(p) / (math.factorial(r) * math.factorial(p - r))


ai = A.pop()

target = ai / 2
aj = A[0]
for i in range(1, len(A)):
    if abs(A[i] - target) <= abs(aj - target):
        aj = A[i]

print(ai, aj)
