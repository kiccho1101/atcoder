H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))

field = [[0] * W for _ in range(H)]
x = 0
y = 0
dx = 1
for i in range(len(A)):
    a = i + 1
    num = A[i]
    while num > 0:
        field[y][x] = a
        x += dx
        if x == -1 or x == W:
            if x == -1:
                x = 0
            if x == W:
                x = W - 1
            dx = -dx
            y += 1
        num -= 1

for row in field:
    print(*row)
