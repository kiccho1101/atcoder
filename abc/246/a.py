from collections import defaultdict


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

xs = defaultdict(int)
ys = defaultdict(int)

xs[x1] += 1
xs[x2] += 1
xs[x3] += 1

ys[y1] += 1
ys[y2] += 1
ys[y3] += 1

for key in xs.keys():
    if xs[key] == 1:
        x = key

for key in ys.keys():
    if ys[key] == 1:
        y = key
print(x, y)
