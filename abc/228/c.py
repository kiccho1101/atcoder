N, K = map(int, input().split())

scores = [(sum(map(int, input().split())), i) for i in range(N)]

scores.sort(reverse=True)
min_score = scores[K - 1][0]

ok = {}
for i in range(N):
    score, idx = scores[i]
    if score + 300 >= min_score:
        ok[idx] = True
    else:
        ok[idx] = False

for i in range(N):
    if ok[i]:
        print("Yes")
    else:
        print("No")
