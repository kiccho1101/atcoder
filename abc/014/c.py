MAX_X = 10 ** 6

cum = [0] * (MAX_X + 2)

N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    cum[a] += 1
    cum[b + 1] -= 1

for i in range(MAX_X):
    cum[i + 1] += cum[i]

print(max(cum))
