N, M = map(int, input().split())

B = [list(map(int, input().split())) for _ in range(N)]

b = B[0][0]

I = b // 7
J = b - 7 * I

flag = True
for i in range(N):
    for j in range(M):
        target = 7 * (I + i) + (J + j)
        if B[i][j] != target:
            flag = False

if flag:
    print("Yes")
else:
    print("No")
