N, Q = map(int, input().split())

A = list(map(int, input().split()))
xs = list(map(int, input().split()))


for x in xs:
    ans = 0

    right = 0
    s = 0
    for left in range(len(A)):
        while right < len(A) and s + A[right] <= x:
            s += A[right]
            right += 1

        ans += right - left

        if right == left:
            right += 1
        else:
            s -= A[left]
    print(ans)
