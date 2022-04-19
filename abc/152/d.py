import math

N = int(input())

# dp[i][j]: 先頭がiで末尾がjである数字の数
dp = [[0] * 10 for _ in range(10)]

for i in range(1, N + 1):
    keta = int(math.log10(i))
    start = i // (10 ** keta) if keta != 0 else i
    end = i % 10
    dp[start][end] += 1

ans = 0
for a_end in range(1, 10):
    for b_end in range(1, 10):
        num_a = dp[b_end][a_end]
        num_b = dp[a_end][b_end]
        ans += num_a * num_b

print(ans)
