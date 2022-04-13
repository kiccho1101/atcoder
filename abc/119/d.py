a, b, q = map(int, input().split())
A = [] + [int(input()) for _ in range(a)]
B = [int(input()) for _ in range(b)]
X = [int(input()) for _ in range(q)]

A.sort()
B.sort()


def bin_search_left(arr, target):
    left = -1
    right = len(arr)
    while right - left > 1:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid
        else:
            right = mid
    return left


def bin_search_right(arr, target):
    left = -1
    right = len(arr)
    while right - left > 1:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid
    return right


for x in X:
    a_l = bin_search_left(A, x)
    a_r = bin_search_right(A, x)
    b_l = bin_search_left(B, x)
    b_r = bin_search_right(B, x)
    candidates = []
    if a_r < len(A) and b_l >= 0:
        candidates.append(A[a_r] - B[b_l] + min(A[a_r] - x, x - B[b_l]))
    if b_r < len(B) and a_l >= 0:
        candidates.append(B[b_r] - A[a_l] + min(B[b_r] - x, x - A[a_l]))
    if a_r < len(A) and b_r < len(B):
        candidates.append(max(A[a_r], B[b_r]) - x)
    if a_l >= 0 and b_l >= 0:
        candidates.append(x - min(A[a_l], B[b_l]))
    ans = min(candidates)
    print(ans)
