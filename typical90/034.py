from collections import defaultdict


N, K = map(int, input().split())
a = list(map(int, input().split()))

left = 0
right = 0
ans = 0
counter = defaultdict(int)
counter[a[0]] += 1
while right < N:
    unique_num = len(counter)
    if unique_num <= K:
        ans = max(ans, right - left + 1)
        right += 1
        if right < N:
            counter[a[right]] += 1
    else:
        counter[a[left]] -= 1
        if counter[a[left]] == 0:
            del counter[a[left]]
        left += 1

print(ans)
