N = int(input())

db = {1: {}, 2: {}}
for i in range(N):
    c, p = map(int, input().split())
    db[c][i + 1] = p


Q = int(input())
qs = []
max_i = -1
for _ in range(Q):
    l, r = map(int, input().split())
    qs.append([l, r])
    if max_i < r:
        max_i = r

sum_scores_1 = [0] * (max_i + 1)
sum_scores_2 = [0] * (max_i + 1)
for i in range(max_i):
    sum_scores_1[i + 1] += sum_scores_1[i]
    sum_scores_2[i + 1] += sum_scores_2[i]

    if i + 1 in db[1]:
        sum_scores_1[i + 1] += db[1][i + 1]
    if i + 1 in db[2]:
        sum_scores_2[i + 1] += db[2][i + 1]

for q in qs:
    score_1 = sum_scores_1[q[1]] - sum_scores_1[q[0] - 1]
    score_2 = sum_scores_2[q[1]] - sum_scores_2[q[0] - 1]
    print(score_1, score_2)
