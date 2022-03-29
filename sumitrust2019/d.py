N = int(input())
S = input()

ans = 0
for i in range(0, 10):
    idx_i = S.find(str(i))
    if idx_i == -1 or idx_i >= N - 2:
        continue
    for j in range(0, 10):
        idx_j = S.find(str(j), idx_i + 1)
        if idx_j == -1 or idx_j >= N - 1:
            continue
        for k in range(0, 10):
            idx_k = S.find(str(k), idx_j + 1)
            if idx_k != -1:
                ans += 1

print(ans)
