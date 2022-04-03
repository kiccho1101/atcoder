H, W, K = map(int, input().split())
field = [list(input()) for _ in range(H)]

no_straw_hs = []
straw_hs = []
ans = [[0] * W for _ in range(H)]
num = 1
for h in range(H):
    if "#" not in field[h]:
        no_straw_hs.append(h)
        continue
    first = True
    for w in range(W):
        if field[h][w] == "#":
            if first:
                first = False
            else:
                num += 1
        ans[h][w] = num
    num += 1
    straw_hs.append(h)


def bin_search(A, target):
    left = -1
    right = len(A)
    while right - left > 1:
        mid = (left + right) // 2
        if A[mid] > target:
            right = mid
        else:
            left = mid
    return right


for h in no_straw_hs:
    th_idx = bin_search(straw_hs, h)
    if not th_idx < len(straw_hs):
        th_idx = -1
    th = straw_hs[th_idx]
    for w in range(W):
        ans[h][w] = ans[th][w]


for row in ans:
    print(*row)
