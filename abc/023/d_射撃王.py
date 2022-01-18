N = int(input())

H = []
S = []
for _ in range(N):
    h, s = map(int, input().split())
    H.append(h)
    S.append(s)


def max_is_less_than_mid(mid, H, S, N) -> bool:
    heights = [0] * N

    for i in range(N):
        j = (mid - H[i]) // S[i] + 1
        if j > 0:
            heights[min(j, N) - 1] += 1

    flag = True
    current = N - 1
    for i in range(N - 1, -1, -1):
        while current >= 0 and heights[current] == 0:
            current -= 1
        if current < i:
            flag = False
            break
        heights[current] -= 1

    return flag


left = min(H) - 1
right = max([H[i] + S[i] * (N - 1) for i in range(N)]) + 1
while right - left > 1:
    mid = left + (right - left) // 2

    flag = max_is_less_than_mid(mid, H, S, N)
    if flag:
        right = mid
    else:
        left = mid

print(left + 1)
