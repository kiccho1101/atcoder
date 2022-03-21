N = int(input())
A = list(map(int, input().split()))

ans = 0
right = 0
visited = set()
for left in range(len(A)):
    while right < len(A) and A[right] not in visited:
        visited.add(A[right])
        right += 1

    ans = max(ans, len(visited))

    if left == right:
        right += 1
    else:
        visited.remove(A[left])

print(ans)
