_ = input()

A = list(map(int, input().split()))
mod = 10 ** 9 + 7

s = 0
ss = sum(A[:-1])
for i in range(len(A) - 1, -1, -1):
    s += A[i] * ss
    if i > 0:
        ss -= A[i - 1]
print(s % mod)
