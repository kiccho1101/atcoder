N, M, P = map(int, input().split())
edges = []
for _ in range(M):
    s, e, w = map(int, input().split())
    s -= 1
    e -= 1
    edges.append((s, e, -w))

INF = 10 ** 18
scores = [INF] * N
scores[0] = 0
for i in range(N):
    for j in range(M):
        s, e, w = edges[j]
        if scores[s] != INF and scores[e] > scores[s] + w + P:
            scores[e] = scores[s] + w + P

            if i == N - 1:
                scores[e] = -INF
                updated = True
                while updated:
                    updated = False
                    for ss, ee, ww in edges:
                        if scores[ee] != -INF and scores[ss] == -INF:
                            scores[ee] = -INF
                            updated = True

ans = -scores[-1]
if ans == INF:
    print(-1)
elif ans < 0:
    print(0)
else:
    print(ans)
