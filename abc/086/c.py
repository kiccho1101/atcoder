N = int(input())

points = [(0, [0, 0])]
for _ in range(N):
    t, x, y = map(int, input().split())
    points.append((t, [x, y]))

points.sort()

flag = True
for i in range(len(points) - 1):
    x1, y1 = points[i][1]
    x2, y2 = points[i + 1][1]

    dt = points[i + 1][0] - points[i][0]
    dist = abs(x2 - x1) + abs(y2 - y1)

    if dist > dt or (dt - dist) % 2 != 0:
        flag = False
        break


if flag:
    print("Yes")
else:
    print("No")
