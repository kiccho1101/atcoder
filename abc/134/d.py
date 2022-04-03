N = int(input())
a = list(map(int, input().split()))
b = [0] * N

for i in reversed(range(N)):

    cnt = 0
    for j in range(i, N, i + 1):
        cnt += b[j]
    if (cnt - a[i]) % 2 == 1:
        b[i] = 1

print(sum(b))
print(" ".join([str(i + 1) for i in range(N) if b[i] == 1]))
