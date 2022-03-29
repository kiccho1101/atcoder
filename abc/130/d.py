N, K = map(int, input().split())
A = list(map(int, input().split()))

right = 0
s = 0
ans = 0
for left in range(len(A)):
    while right < len(A) and s + A[right] < K:
        s += A[right]
        right += 1

    ans += len(A) - right

    if right == left:
       l right += 1
    else:
        s -= A[left]

print(ans)
