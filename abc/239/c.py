exists = {}
ds = ((2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1))

x1, y1, x2, y2 = map(int, input().split())

for dx, dy in ds:
    key = str((x1 + dx, y1 + dy))
    exists[key] = True

flag = False
for dx, dy in ds:
    key = str((x2 + dx, y2 + dy))
    if key in exists:
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")
