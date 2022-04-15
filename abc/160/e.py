INF = 10 ** 18
X, Y, A, B, C = map(int, input().split())
P = list(map(int, input().split())) + [-INF]
Q = list(map(int, input().split())) + [-INF]
R = list(map(int, input().split())) + [-INF]

P.sort()
Q.sort()
R.sort()

ans = 0
x = 0
y = 0
r = 0
while x + y + r < X + Y:
    if x == X:
        if Q[-1] >= R[-1]:
            ans += Q.pop()
        else:
            ans += R.pop()
        y += 1
    elif y == Y:
        if P[-1] >= R[-1]:
            ans += P.pop()
        else:
            ans += R.pop()
        x += 1
    else:
        if P[-1] >= Q[-1] and P[-1] >= R[-1]:
            ans += P.pop()
            x += 1
        elif Q[-1] >= P[-1] and Q[-1] >= R[-1]:
            ans += Q.pop()
            y += 1
        else:
            ans += R.pop()
            r += 1

print(ans)
