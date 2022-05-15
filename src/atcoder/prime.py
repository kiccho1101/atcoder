from typing import List


def get_primes(n: int) -> List[int]:
    is_prime = [True for _ in range(n + 1)]
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, n + 1):
        if is_prime[i]:
            j = i + i
            while j <= n:
                is_prime[j] = False
                j += i
    primes = [i for i in range(1, n + 1) if is_prime[i]]
    return primes


if __name__ == "__main__":
    print(get_primes(100))
