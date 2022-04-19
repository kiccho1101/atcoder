import itertools


N = int(input())

ans = 0
for i in range(3, 10):
    for a in itertools.product((3, 5, 7), repeat=i):
        if 3 in a and 5 in a and 7 in a:
            n = int("".join(map(str, a)))
            if n <= N:
                ans += 1

print(ans)
