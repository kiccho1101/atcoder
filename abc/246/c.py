N, K, X = map(int, input().split())

A = list(map(int, input().split()))


for i in range(len(A)):
    k = A[i] // X
    if K >= k:
        A[i] -= k * X
        K -= k
    else:
        A[i] -= K * X
        K = 0
    if K == 0:
        break

A.sort(reverse=True)
for i in range(min(K, len(A))):
    A[i] = 0

print(sum(A))
