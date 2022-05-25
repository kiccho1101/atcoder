N = int(input())

s = 0
for i in range(1, 10):
    for j in range(1, 10):
        s += i * j

for i in range(1, 10):
    for j in range(1, 10):
        if s - i * j == N:
            print("{} x {}".format(i, j))
