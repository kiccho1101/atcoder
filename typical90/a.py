_, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))


def mid_is_bigger_than_ans(mid, K, A):
    a_list = [0] + A + [L]

    current = 0
    cnt = 0
    for i in range(1, len(a_list)):
        length = a_list[i] - a_list[current]
        if length > mid:
            cnt += 1
            current = i

    return cnt >= K + 1


left = -1
right = L + 1
while right - left > 1:
    mid = left + (right - left) // 2
    if mid_is_bigger_than_ans(mid, K, A):
        left = mid
    else:
        right = mid

print(left + 1)
