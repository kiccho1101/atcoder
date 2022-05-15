N = int(input())

A = sorted([int(input()) for _ in range(N)])


def calc_diffsum(a):
    ret = 0
    for i in range(len(a) - 1):
        ret += abs(a[i] - a[i + 1])
    return ret


a_1 = []
a_2 = []


if N % 2 == 0:

    for i in range(len(A) // 2 - 1):
        a_1.append(A[i])
        a_1.append(A[-(i + 1)])

        a_2.append(A[-(i + 1)])
        a_2.append(A[i])

    left = len(A) // 2 - 1
    right = len(A) // 2

    ans = max(
        calc_diffsum([A[left]] + a_1 + [A[right]]),
        calc_diffsum([A[right]] + a_1 + [A[left]]),
        calc_diffsum([A[left], A[right]] + a_1),
        calc_diffsum([A[right], A[left]] + a_1),
        calc_diffsum(a_1 + [A[left], A[right]]),
        calc_diffsum(a_1 + [A[right], A[left]]),
        calc_diffsum([A[left]] + a_2 + [A[right]]),
        calc_diffsum([A[right]] + a_2 + [A[left]]),
        calc_diffsum([A[left], A[right]] + a_2),
        calc_diffsum([A[right], A[left]] + a_2),
        calc_diffsum(a_2 + [A[left], A[right]]),
        calc_diffsum(a_2 + [A[right], A[left]]),
    )
    print(ans)

else:
    for i in range(len(A) // 2):
        a_1.append(A[i])
        a_1.append(A[-(i + 1)])

        a_2.append(A[-(i + 1)])
        a_2.append(A[i])

    mid = N // 2

    ans = max(
        calc_diffsum([A[mid]] + a_1),
        calc_diffsum(a_1 + [A[mid]]),
        calc_diffsum([A[mid]] + a_2),
        calc_diffsum(a_2 + [A[mid]]),
    )
    print(ans)
