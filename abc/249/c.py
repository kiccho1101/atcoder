from collections import defaultdict
import itertools


N, K = map(int, input().split())
ss = [input() for _ in range(N)]

ans = 0
for bit in itertools.product((0, 1), repeat=N):
    char_num = defaultdict(int)
    for i, b in enumerate(bit):
        if b == 1:
            chars = ss[i]
            for j in range(26):
                c = chr(ord("a") + j)
                if chars.find(c) != -1:
                    char_num[c] += 1

    num = 0
    for c, n in char_num.items():
        if n == K:
            num += 1
    ans = max(ans, num)

print(ans)
