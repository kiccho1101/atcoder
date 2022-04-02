N = int(input())


def f(a, b):
    return a * a * a + a * a * b + a * b * b + b * b * b


def bin_search(a, target):
    left = -1
    right = 10 ** 6 + 1
    while right - left > 1:
        mid = (left + right) // 2
        if f(a, mid) < target:
            left = mid
        else:
            right = mid
    return right


ans = float("inf")
for a in range(0, 10 ** 6 + 1):
    b = bin_search(a, N)
    ans = min(ans, f(a, b))

print(ans)
