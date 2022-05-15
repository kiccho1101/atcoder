N, W = map(int, input().split())

A = list(map(int, input().split()))

ans = set()

# 1個
if N >= 1:
    for i in range(N):
        if A[i] <= W:
            ans.add(A[i])

# 2個
if N >= 2:
    for i in range(N - 1):
        for j in range(i + 1, N):
            s = A[i] + A[j]
            if s <= W:
                ans.add(s)

# 3個
if N >= 3:
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                s = A[i] + A[j] + A[k]
                if s <= W:
                    ans.add(s)

print(len(ans))
