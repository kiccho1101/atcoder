from collections import defaultdict


N, Q = list(map(int, input().split()))

a_list = list(map(int, input().split()))

db = defaultdict(dict)
max_num = defaultdict(int)
for i in range(len(a_list)):
    a = a_list[i]
    max_num[a] += 1
    db[a][max_num[a]] = i + 1

xs = []
ks = []
for i in range(Q):
    x, k = list(map(int, input().split()))
    xs.append(x)
    ks.append(k)

for i in range(len(xs)):
    x, k = xs[i], ks[i]
    if x in db and k in db[x]:
        print(db[x][k])
    else:
        print(-1)
