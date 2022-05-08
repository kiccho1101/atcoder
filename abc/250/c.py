N, Q = map(int, input().split())
X = [int(input()) for _ in range(Q)]
A = [i for i in range(1, N + 1)]
pos = {i: i - 1 for i in range(1, N + 1)}

for x in X:
    if pos[x] == N - 1:
        A[N - 1], A[N - 2] = A[N - 2], A[N - 1]
        pos[A[N - 1]] = N - 1
        pos[A[N - 2]] = N - 2
    else:
        a = pos[x]
        a_val = A[a]
        b = pos[x] + 1
        b_val = A[b]
        A[pos[x]], A[pos[x] + 1] = A[pos[x] + 1], A[pos[x]]
        pos[a_val] = b
        pos[b_val] = a

print(*A)
