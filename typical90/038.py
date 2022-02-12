def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


a, b = map(int, input().split())

g = gcd(a, b)

lcm = a * b // g

if lcm > 10 ** 18:
    print("Large")
else:
    print(lcm)
