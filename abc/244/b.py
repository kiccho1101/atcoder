N = int(input())
T = input()

ds = [(1, 0), (0, -1), (-1, 0), (0, 1)]
di = 0
x = 0
y = 0
for t in T:
    if t == "S":
        x += ds[di][0]
        y += ds[di][1]
    if t == "R":
        di += 1
        if di == 4:
            di = 0

print(x, y)
