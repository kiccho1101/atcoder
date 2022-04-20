N = int(input())
A = [int(input()) for _ in range(N)]


def lower_bound(A, target):
    left = -1
    right = len(A)
    while right - left > 1:
        mid = (left + right) // 2
        if A[mid] >= target:
            right = mid
        else:
            left = mid
    return right


st = []
for a in A:
    if len(st) == 0:
        st.append(a)
    else:
        i = lower_bound(st, a)
        if i < len(st):
            st[i] = a
        else:
            st.append(a)

print(len(st))
