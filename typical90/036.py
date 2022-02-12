N, Q = map(int, input().split())
sums = []
diffs = []
points = []

for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))
    sums.append(x + y)
    diffs.append(x - y)

sums.sort()
diffs.sort()

for _ in range(Q):
    q = int(input())
    q -= 1

    sumi = points[q][0] + points[q][1]
    diffi = points[q][0] - points[q][1]

    print(
        max(
            abs(sums[0] - sumi),
            abs(sums[-1] - sumi),
            abs(diffs[0] - diffi),
            abs(diffs[-1] - diffi),
        )
    )
