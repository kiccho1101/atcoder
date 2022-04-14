change = 1000 - int(input())

ans = 0
for coin in [500, 100, 50, 10, 5, 1]:
    while change >= coin:
        n = change // coin
        change -= n * coin
        ans += n
print(ans)
