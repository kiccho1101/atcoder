N = int(input())
A = list(map(int, input().split()))

del_a = A[-1]
for i in range(len(A) - 1):
    if A[i] > A[i + 1]:
        del_a = A[i]
        break

print(*[a for a in A if a != del_a])
