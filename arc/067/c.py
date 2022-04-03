from collections import defaultdict


class Solver:
    def __init__(self):
        self.counter = defaultdict(int)

    def prime_factorization(self, n):
        while n % 2 == 0:
            self.counter[2] += 1
            n //= 2

        f = 3
        while f * f <= n:
            if n % f == 0:
                self.counter[f] += 1
                n //= f
            else:
                f += 2
        if n != 1:
            self.counter[n] += 1

    def solve(self, N):
        for i in range(1, N + 1):
            self.prime_factorization(i)
        ans = 1
        MOD = 10 ** 9 + 7
        for v in self.counter.values():
            ans *= v + 1
            ans %= MOD
        return ans


N = int(input())
ans = Solver().solve(N)
print(ans)
