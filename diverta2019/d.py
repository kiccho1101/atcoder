N = int(input())

for i in range(1, N + 1):
    if N // i == N % i:
        print(i)
