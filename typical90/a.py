_, L = list(map(int, input().split()))
K = int(input())
a_list = list(map(int, input().split()))


def ans_is_bigger_than_mid(a_list, mid, K):
    cnt = 0
    pre = 0
    for i in range(len(a_list)):
        if a_list[i] - pre >= mid and L - a_list[i] >= mid:
            cnt += 1
            pre = a_list[i]
    return cnt >= K


left = -1
right = L + 1

while right - left > 1:
    mid = left + (right - left) // 2

    a = ans_is_bigger_than_mid(a_list, mid, K)
    if a:
        left = mid
    else:
        right = mid

print(left)
