_ = input()

A = list(map(int, input().split()))
A.sort()

n = int(input())
ratings = [int(input()) for _ in range(n)]


def binary_search(A, r):
    left = 0
    right = len(A) - 1
    while right - left > 1:
        mid = (left + right) // 2
        # print(left, right, mid, A[mid], r)
        if A[mid] > r:
            right = mid
        else:
            left = mid
    return left, right


for r in ratings:
    left, right = binary_search(A, r)
    print(min(abs(A[left] - r), abs(A[right] - r)))
