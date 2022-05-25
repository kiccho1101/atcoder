import heapq
import sys

N = int(input())

# 頂点1から最も遠い点を探す
max_point = -1
max_dist = -1
for i in range(2, N + 1):
    print("? {} {}".format(1, i))
    sys.stdout.flush()
    dist = int(input())
    if dist > max_dist:
        max_point = i
        max_dist = dist

# 頂点max_pointから最も遠い点を探す
ans = -1
for i in range(1, N + 1):
    if i != max_point:
        print("? {} {}".format(max_point, i))
        sys.stdout.flush()
        dist = int(input())
        if dist > ans:
            ans = dist


print("! {}".format(ans))
