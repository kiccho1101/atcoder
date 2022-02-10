N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

s = 0
for i in range(len(A)):
    s += abs(A[i] - B[i])
print(s)
