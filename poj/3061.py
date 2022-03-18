Q = int(input())

N, S = map(int, input().split())

for _ in range(Q):
    A = list(map(int, input().split()))

    ans = 10 ** 18

    right = 0
    s = 0
    for left in range(len(A)):
        if right < len(A) and s < S:
            s += A[right]
            right += 1

        if s < S:
            break
        ans = min(ans, right - left)

        if right == left:
            right += 1
        else:
            s -= A[left]

    if ans == 10 ** 18:
        print(0)
    else:
        print(ans)
