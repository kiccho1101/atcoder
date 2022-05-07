N, K, A = map(int, input().split())

if N - A + 1 < K:
    K -= N - A + 1
else:
    print(A + K - 1)
    exit()

while True:
    if K <= N:
        print(K)
        exit()
    K -= N
