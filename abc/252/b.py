N, K = map(int, input().split())
A = list(map(int, input().split()))
B = set(map(int, input().split()))

ans = "No"
A_max = max(A)
for i in range(N):
    if A[i] == A_max:
        if i + 1 in B:
            ans = "Yes"
            break


print(ans)
