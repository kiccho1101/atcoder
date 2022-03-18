N, K = map(int, input().split())

A = list(map(int, input().split()))

ans = 0
queue = {}
right = 0
for left in range(len(A)):
    while right < len(A) and len(queue) <= K:
        if A[right] not in queue:
            queue[A[right]] = 0
        queue[A[right]] += 1
        right += 1

    if len(queue) <= K:
        ans = max(ans, right - left)
    else:
        ans = max(ans, right - left - 1)

    if right == left:
        right += 1
    else:
        queue[A[left]] -= 1
        if queue[A[left]] == 0:
            del queue[A[left]]

print(ans)
