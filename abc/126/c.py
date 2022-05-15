N, K = map(int, input().split())

pows = []
for i in range(1, N + 1):
    cnt = 0
    j = i
    while j <= K - 1:
        j *= 2
        cnt += 1
    pows.append(cnt)

max_pow = max(pows)

a = 0
for i in range(len(pows)):
    a += pow(2, max_pow - pows[i])

b = pow(2, max_pow)
ans = a / b / N
print(ans)
