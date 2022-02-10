N = int(input())

a, b, c = map(int, input().split())

MAX_SUM = 9999

max_z = N // c + 1


ans = 10 ** 18
for x in range(MAX_SUM + 1):
    for y in range(MAX_SUM + 1 - x):
        z = (N - a * x - b * y) / c
        if not z.is_integer():
            continue
        s = x + y + z
        if s > MAX_SUM or z > max_z or z < 0:
            break
        ans = min(ans, s)
print(int(ans))
