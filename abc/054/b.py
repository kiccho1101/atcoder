N, M = map(int, input().split())

A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(M)]

for A_y in range(N - M + 1):
    for A_x in range(N - M + 1):
        flag = True
        for B_y in range(M):
            for B_x in range(M):
                y = A_y + B_y
                x = A_x + B_x
                if A[y][x] != B[B_y][B_x]:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            print("Yes")
            exit()

print("No")
