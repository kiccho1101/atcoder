N = int(input())
A = list(map(int, input().split()))


def get_rating(a):
    for i in range(8):
        if i * 400 <= a <= (i + 1) * 400 - 1:
            return i
    return 9


ans = set()
num = 0
for a in A:
    r = get_rating(a)
    if r == 9:
        num += 1
    else:
        ans.add(r)

print(
    len(ans) if num == 0 else max(1, len(ans)),
    len(ans) + num,
)
