import itertools


N = int(input())
F = [list(map(int, input().split())) for i in range(N)]
P = [list(map(int, input().split())) for i in range(N)]

ans = -(10 ** 18)

for bits in itertools.product((0, 1), repeat=10):
    if bits == tuple([0] * 10):
        continue

    profit = 0
    for f, p in zip(F, P):
        count: int = 0
        for i, bit in enumerate(bits):
            if bit == 1 and f[i] == 1:
                count += 1
        profit += p[count]

    ans = max(ans, profit)

print(ans)
