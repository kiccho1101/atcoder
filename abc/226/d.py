def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


N = int(input())
xy = [tuple(map(int, input().split())) for _ in range(N)]


fra = set()
for i in range(N):
    for j in range(N):
        if i != j:
            x1, y1 = xy[i]
            x2, y2 = xy[j]
            dx = x2 - x1
            dy = y2 - y1

            g = abs(gcd(dx, dy))
            dx //= g
            dy //= g

            fra.add(f"{dx},{dy}")

print(len(fra))
