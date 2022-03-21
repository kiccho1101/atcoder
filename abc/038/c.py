N = int(input())

A = list(map(int, input().split()))

ans = 0
right = 0
for left in range(len(A)):
    while right < len(A) - 1 and A[right] < A[right + 1]:
        right += 1

    ans += right - left + 1

    if right == left:
        right += 1

print(ans)
