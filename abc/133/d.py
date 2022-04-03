N = int(input())
A = list(map(int, input().split()))

x = [-1] * N

s = 0
for i, a in enumerate(A):
    if i % 2 == 0:
        s += a
    else:
        s -= a

x[0] = s // 2
x[N - 1] = A[N - 1] - x[0]

for i in range(N - 2, 0, -1):
    x[i] = A[i] - x[i + 1]

print(*[2 * _x for _x in x])
