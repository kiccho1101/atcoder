from collections import deque


N = int(input())
A = list(map(int, input().split()))

nums = deque()
counts = [deque() for _ in range(2 * (10 ** 5) + 1)]

ans = 0
for i in range(N):
    a = A[i]

    # 前回と同じ数字の場合
    if len(nums) > 0 and a == nums[-1]:
        counts[a].append(counts[a].pop() + 1)
        if counts[a][-1] == a:
            nums.pop()
            c = counts[a].pop()
            ans -= c
        ans += 1

    else:
        nums.append(a)
        counts[a].append(1)
        ans += 1

    print(ans)
