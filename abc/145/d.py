MOD = 10 ** 9 + 7
X, Y = map(int, input().split())
N = 10 ** 6
ans_a = -1
ans_b = -1
for a in range(N + 1):
    if X - 2 * Y + 3 * a == 0:
        ans_a = a
        ans_b = Y - 2 * ans_a
        break

if ans_a == -1:
    print(0)
    exit()


def nCr_mod(n, r, mod):
    upper = 1
    for i in range(n - r + 1, n + 1):
        upper *= i
        upper %= mod

    below = 1
    for i in range(1, r + 1):
        below *= i
        below %= mod

    below_inv = pow(below, -1, mod)

    return upper * below_inv % mod


print(nCr_mod(ans_a + ans_b, ans_a, MOD))
