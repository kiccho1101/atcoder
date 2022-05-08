import collections


N = int(input())
V = list(map(int, input().split()))

f_cnt = collections.Counter()
s_cnt = collections.Counter()
for i, v in enumerate(V):
    if i % 2 == 0:
        f_cnt[v] += 1
    else:
        s_cnt[v] += 1

f_cnt = f_cnt.most_common()
s_cnt = s_cnt.most_common()

if f_cnt[0][0] != s_cnt[0][0]:
    ans = N - f_cnt[0][1] - s_cnt[0][1]
    print(ans)
    exit()

n1 = 0
n2 = 0
if len(f_cnt) > 1:
    n1 = f_cnt[1][1]
if len(s_cnt) > 1:
    n2 = s_cnt[1][1]
print(min(N - f_cnt[0][1] - n2, N - s_cnt[0][1] - n1))
