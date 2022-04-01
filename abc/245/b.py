N = int(input())
A = list(map(int, input().split()))

A = [a for a in A if a >= 0]
A.sort()

if A[0] != 0:
    print(0)
    exit()

for i in range(1, len(A)):
    if A[i] - A[i - 1] > 1:
        print(A[i - 1] + 1)
        exit()

print(A[-1] + 1)
