N = int(input())

xs = []
ys = []
for _ in range(N):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

S = input()

INF = 10 ** 18
y_lr = {}
for i in range(N):
    if ys[i] not in y_lr:
        y_lr[ys[i]] = {"l": INF, "r": -INF}

    if S[i] == "L":
        y_lr[ys[i]]["r"] = max(y_lr[ys[i]]["r"], xs[i])
    if S[i] == "R":
        y_lr[ys[i]]["l"] = min(y_lr[ys[i]]["l"], xs[i])

for y in y_lr.values():
    if y["l"] < y["r"]:
        exit(print("Yes"))
print("No")
