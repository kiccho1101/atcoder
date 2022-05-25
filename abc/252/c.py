import collections

N = int(input())
S = [input() for _ in range(N)]

INF = 10 ** 18
ans = INF
for i in range(10):
    idxs = [s.find(str(i)) for s in S]
    counter = collections.Counter(idxs)
    mc = counter.most_common()
    if mc[0][1] == 1:
        sec = max(idxs)
    else:
        max_cnt = mc[0][1]
        sec = max([10 * (cnt - 1) + idx for idx, cnt in mc if cnt == max_cnt])
    ans = min(ans, sec)

print(ans)
