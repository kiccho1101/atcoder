N, K = map(int, input().split())

scores = []
for _ in range(N):
    a, b = map(int, input().split())
    scores.append(b)
    scores.append(a - b)

print(sum(sorted(scores, reverse=True)[:K]))
