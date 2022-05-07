S = list(input())
n = len(S)
A = [0] * (n + 1)

for i in range(n):
    if S[i] == "<":
        A[i + 1] = max(A[i + 1], A[i] + 1)

for i in reversed(range(n)):
    if S[i] == ">":
        A[i] = max(A[i], A[i + 1] + 1)

print(sum(A))
