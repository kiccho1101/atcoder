N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

# y = x + b1
b1 = B - A

# y = -x + b2
b2 = B + A


def ok(y, x, b1, b2):
    if y == x + b1 or y == -x + b2:
        return "#"
    return "."


for x in range(P, Q + 1):
    ans = ""
    for y in range(R, S + 1):
        ans += ok(y, x, b1, b2)
    print(ans)
