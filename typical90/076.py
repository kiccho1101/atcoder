from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

s = sum(A)

if not (s / 10).is_integer():
    exit(print("No"))


A.append(A[0])
N = len(A)
target = s // 10

left = 0
a = 0
for right in range(N):
    a += A[right]
    if a == target:
        exit(print("Yes"))
    while right - left > 0:
        print(left, right, a)
        if a == target:
            exit(print("Yes"))

        elif a > target:
            a -= A[left]
            left += 1

        elif a < target:
            break

print("No")
