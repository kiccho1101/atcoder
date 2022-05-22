N = int(input())
A = list(map(int, input().split()))

ans = 0
mode = None
last = None
for a in A:
    if last is not None:
        if mode == "asc":
            if a < last:
                ans += 1
                mode = None
        elif mode == "desc":
            if a > last:
                ans += 1
                mode = None
        else:
            if a > last:
                mode = "asc"
            elif a < last:
                mode = "desc"

    last = a

print(ans + 1)
