n, k = map(int, input().split())

for i in range(1, 50):
    if pow(k, i - 1) <= n < pow(k, i):
        print(i)
        exit()
