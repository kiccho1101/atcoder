import itertools


N, M = map(int, input().split())
xyz = [tuple(map(int, input().split())) for _ in range(N)]

ans = -1
for bit in itertools.product((0, 1), repeat=3):
    xyz_tmp = []
    for i in range(N):
        x, y, z = xyz[i]
        tmp = 0
        if bit[0] == 1:
            tmp += x
        else:
            tmp -= x
        if bit[1] == 1:
            tmp += y
        else:
            tmp -= y
        if bit[2] == 1:
            tmp += z
        else:
            tmp -= z
        xyz_tmp.append(tmp)
    xyz_tmp.sort(reverse=True)
    ans = max(ans, sum(xyz_tmp[:M]))

print(ans)
