N = int(input())

keta = len(str(N))

X = 998244353


def nC2(n):
    return n * (n - 1) // 2


ans = N
for k in range(1, 20):
    bottom = 10 ** (k - 1)
    top = 10 ** k

    if N < bottom:
        break
    elif top <= N:
        ans += nC2(top - bottom)
    else:
        ans += nC2(N + 1 - bottom)

print(ans % X)
