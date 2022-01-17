_ = input()

hs = list(map(int, input().split()))

current = 0
for h in hs:
    if current < h:
        current = h
    else:
        break
print(current)
