def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


a, b, c = map(int, input().split())

gcd_ab = gcd(a, b)
gcd_abc = gcd(gcd_ab, c)

ans = (a // gcd_abc - 1) + (b // gcd_abc - 1) + (c // gcd_abc - 1)

print(ans)
