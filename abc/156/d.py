n, a, b = map(int, input().split())

MOD = 10 ** 9 + 7
ans = 0


def nCr_mod(n, r, mod):
    bunsi = 1
    for i in range(n - r + 1, n + 1):
        bunsi *= i
        bunsi %= mod

    bunbo = 1
    for i in range(1, r + 1):
        bunbo *= i
        bunbo %= mod

    bunbo_inv = pow(bunbo, -1, mod)
    return bunsi * bunbo_inv % mod


ans += pow(2, n, MOD)
ans -= 1
ans -= nCr_mod(n, a, MOD)
ans -= nCr_mod(n, b, MOD)

print(ans)
