A = list(map(int, input().split()))

b = A[1]
if b == sorted(A)[1]:
    print("Yes")
else:
    print("No")
