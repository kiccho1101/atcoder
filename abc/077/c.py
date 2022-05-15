N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))


def bisect_left(a, target):
    left = -1
    right = len(a)
    while right - left > 1:
        mid = (left + right) // 2
        if a[mid] > target:
            right = mid
        else:
            left = mid
    return right


B_pos = [0] * N
for i in range(N):
    idx = bisect_left(C, B[i])
    B_pos[i] = N - idx

for i in reversed(range(N)):
    if i + 1 < N:
        B_pos[i] += B_pos[i + 1]

ans = 0
for i in range(N):
    idx = bisect_left(B, A[i])
    if idx < N:
        ans += B_pos[idx]

print(ans)
