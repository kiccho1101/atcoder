from collections import defaultdict


class Fibonacci:
    def __init__(self):
        self.memo = {}
        self.done = defaultdict(lambda: False)

    def fib_memo(self, n: int):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if self.done[n]:
            return self.memo[n]
        self.done[n] = True
        self.memo[n] = self.fib_memo(n - 1) + self.fib_memo(n - 2)
        return self.memo[n]

    def fib_dp(self, n: int):
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


f = Fibonacci()
print(f.fib_memo(10), f.fib_dp(10))
