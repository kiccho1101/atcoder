N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

stock = 0
needed = 0
for i in range(N):
    if A[i] < B[i]:
        stock += (B[i] - A[i]) // 2
    elif A[i] > B[i]:
        needed += A[i] - B[i]

if stock >= needed:
    print("Yes")
else:
    print("No")
