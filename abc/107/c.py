N, K = map(int, input().split())

X = list(map(int, input().split()))
A = []
B = []
for i in range(len(X)):
    if X[i] >= 0:
        A.append(X[i])
    else:
        B.insert(0, X[i])

# i: 左にi回行く
ans = float("inf")
for i in range(K + 1):
    if i == 0:
        if len(A) >= K:
            ans = min(ans, A[K - 1])
    elif i == K:
        if len(B) >= K:
            ans = min(ans, abs(B[K - 1]))
    else:
        if len(B) >= i and len(A) >= K - i:
            a = A[K - i - 1]
            b = abs(B[i - 1])
            ans = min(ans, 2 * a + b, a + 2 * b)

print(ans)
