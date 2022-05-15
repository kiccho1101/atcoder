N = int(input())
M = 3501

for h in range(1, M):
    for w in range(1, M):
        tmp = 4 * h * w - N * (h + w)
        if tmp > 0:
            if N * h * w % tmp == 0:
                u = N * h * w // tmp
                if u < M:
                    print(h, u, w)
                    exit()
