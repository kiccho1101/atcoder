N, Q = map(int, input().split())
A = list(map(int, input().split()))

qs = [list(map(int, input().split())) for _ in range(Q)]

B = [A[i + 1] - A[i] for i in range(N - 1)]
score = sum(abs(i) for i in B)

for l, r, v in qs:
    l -= 1
    r -= 1
    if l > 0:
        score -= abs(B[l - 1])
        B[l - 1] += v
        score += abs(B[l - 1])
    if r < N - 1:
        score -= abs(B[r])
        B[r] -= v
        score += abs(B[r])
    print(score)
