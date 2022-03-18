H, W = map(int, input().split())

field = [list(input()) for _ in range(H)]

INF = 10 ** 18

# dp[i][j]: The minimum procedures of (i,j) fields
dp = [[INF] * W for _ in range(H)]

dp[0][0] = 1 if field[0][0] == "#" else 0

for y in range(H):
    for x in range(W):
        if x - 1 >= 0:
            if field[y][x - 1] == "." and field[y][x] == "#":
                dp[y][x] = min(dp[y][x], dp[y][x - 1] + 1)
            else:
                dp[y][x] = min(dp[y][x], dp[y][x - 1])
        if y - 1 >= 0:
            if field[y - 1][x] == "." and field[y][x] == "#":
                dp[y][x] = min(dp[y][x], dp[y - 1][x] + 1)
            else:
                dp[y][x] = min(dp[y][x], dp[y - 1][x])

print(dp[H - 1][W - 1])
