N = int(input())

A = list(map(int, input().split()))

cnt = [0] * N

for a in A:
    cnt[a - 1] += 1

for i, c in enumerate(cnt):
    if c < 4:
        print(i + 1)
