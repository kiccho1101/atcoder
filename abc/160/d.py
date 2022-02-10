N, X, Y = map(int, input().split())

X -= 1
Y -= 1

num = [0] * (N - 1)
for i in range(N - 1):
    for j in range(i + 1, N):
        num[min(j - i, abs(X - i) + 1 + abs(j - Y), abs(Y - i) + 1 + abs(j - X))] += 1

for i in range(N - 2):
    print(num[i + 1])
print(0)
