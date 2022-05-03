S = list(input())

ans = 10 ** 18
for target in S:
    cnt = 0
    tmp = S[:]
    while len(set(tmp)) > 1:
        for i in range(len(tmp) - 1):
            if tmp[i] == target or tmp[i + 1] == target:
                tmp[i] = target
        tmp.pop()
        cnt += 1
    ans = min(ans, cnt)

print(ans)
