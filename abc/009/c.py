def val(i, j):
    if s[i] == j:
        return 0
    return (0 if amari_s[j] else 1) + (0 if amari_a[s[i]] else 1)


n, k = map(int, input().split())
(*s,) = map(lambda i: ord(i) - 97, input())
cnt = [0] * 26
for si in s:
    cnt[si] += 1
ans = []
amari_s = [0] * 26
amari_a = [0] * 26
for i in range(n):
    for j in range(26):
        if not cnt[j]:
            continue
        r = val(i, j)
        if k >= r:
            k -= r
            ans.append(j)
            cnt[j] -= 1
            if amari_s[j]:
                amari_s[j] -= 1
            else:
                amari_a[j] += 1
            if amari_a[s[i]]:
                amari_a[s[i]] -= 1
            else:
                amari_s[s[i]] += 1
            break
print("".join(map(lambda i: chr(i + 97), ans)))
