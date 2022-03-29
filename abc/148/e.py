N = int(input())
ans = 0
j = 0
if N % 2 == 0:
    while True:
        a = 10 * pow(5, j)
        ans += N // a
        j += 1
        if a > N:
            break

print(ans)
