import math

A, B = input().split()
A, B = int(A), int(B)
print(math.ceil((B - 1) / (A - 1)))
