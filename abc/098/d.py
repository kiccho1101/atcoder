N = int(input())
A = list(map(int, input().split()))

ans = 0
xor_s = 0
s = 0
right = 0
for left in range(len(A)):
    while right < len(A) and s ^ A[right] == s + A[right]:
        s += A[right]
        right += 1

    ans += right - left

    if right == left:
        right += 1
    else:
        s -= A[left]

print(ans)
