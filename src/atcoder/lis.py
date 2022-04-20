import bisect
from typing import List


def lis(a: List[int]):
    INF = 10 ** 18
    n = len(a)
    dp = [INF] * n
    for i in range(n):
        j = bisect.bisect_left(dp, a[i])
        dp[j] = a[i]
        print(dp)

    return bisect.bisect_left(dp, INF)


if __name__ == "__main__":
    a = [2, 3, 1, 5, 6, 4, 8, 7]
    print(lis(a))
