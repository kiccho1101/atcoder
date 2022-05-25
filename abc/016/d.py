Ax, Ay, Bx, By = map(int, input().split())
N = int(input())
xy = [tuple(map(int, input().split())) for _ in range(N)]

n_points = N


def upper(x, y):
    return y > (Ay - By) / (Ax - Bx) * (x - Bx) + By


def intersect(p1, p2, p3, p4):
    tc1 = (p1[0] - p2[0]) * (p3[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p3[0])
    tc2 = (p1[0] - p2[0]) * (p4[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p4[0])
    td1 = (p3[0] - p4[0]) * (p1[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p1[0])
    td2 = (p3[0] - p4[0]) * (p2[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p2[0])
    return tc1 * tc2 < 0 and td1 * td2 < 0


ans = 0
for i in range(N):
    j = (i + 1) % N
    xi, yi = xy[i]
    xj, yj = xy[j]
    if intersect(xy[i], xy[j], (Ax, Ay), (Bx, By)):
        ans += 1

print(ans // 2 + 1)
