N = int(input())
A = list(map(int, input().split()))
Q = int(input())
qs = [tuple(map(int, input().split())) for _ in range(Q)]


db = {}
for i in range(len(A)):
    if A[i] not in db:
        db[A[i]] = []
    db[A[i]].append(i)


def bisect_right(a, target):
    left = -1
    right = len(a)
    while right - left > 1:
        mid = (left + right) // 2
        if a[mid] > target:
            right = mid
        else:
            left = mid
    return right


def bisect_left(a, target):
    left = -1
    right = len(a)
    while right - left > 1:
        mid = (left + right) // 2
        if a[mid] < target:
            left = mid
        else:
            right = mid
    return right


for L, R, X in qs:
    if X not in db:
        print(0)
    else:
        L -= 1
        R -= 1
        l = bisect_left(db[X], L)
        r = bisect_right(db[X], R)
        print(r - l)
