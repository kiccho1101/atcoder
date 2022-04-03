from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

counter = defaultdict(int)
for a in A:
    counter[a] += 1


def ok(N, counter):
    if N % 2 == 0:
        for i in range(N // 2):
            n = 1 + 2 * i
            if counter[n] != 2:
                return False
    else:
        for i in range((N + 1) // 2):
            n = 2 * i
            if n == 0:
                if counter[n] != 1:
                    return False
            elif counter[n] != 2:
                return False

    return True


MOD = 10 ** 9 + 7
if ok(N, counter):
    print(pow(2, N // 2, MOD))
else:
    print(0)
