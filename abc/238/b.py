_ = input()

A = list(map(int, input().split()))

rads = set([0])
for i, a in enumerate(A):
    to_be_removed = set()
    to_be_added = set()
    for r in rads:
        to_be_removed.add(r)
        rr = r + a
        if rr > 360:
            rr -= 360
        to_be_added.add(rr)
    for r in to_be_removed:
        rads.remove(r)
    for r in to_be_added:
        rads.add(r)
    rads.add(0)
rads.add(360)

rads_list = sorted(list(rads))

max_rad = 0
for i in range(len(rads_list) - 1):
    if rads_list[i + 1] - rads_list[i] > max_rad:
        max_rad = rads_list[i + 1] - rads_list[i]

print(max_rad)
