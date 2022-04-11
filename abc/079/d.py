import collections

H, W = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(10)]

counter = collections.defaultdict(int)
for _ in range(H):
    for a in map(int, input().split()):
        if a != -1 and a != 1:
            counter[a] += 1


for k in range(10):
    for i in range(10):
        for j in range(10):
            mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])


ans = 0
for key in counter.keys():
    ans += mat[key][1] * counter[key]

print(ans)
