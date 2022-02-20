A, B, C, D = map(int, input().split())


def prime(N):
    primes = []
    for i in range(2, N + 1):
        primes.append(i)
        for p in range(2, i):
            if i % p == 0:
                primes.remove(i)
                break
    return primes


is_prime = [False] * 201
for p in prime(200):
    is_prime[p] = True


winner = "Aoki"
for t in range(A, B + 1):
    has_prime = False
    for a in range(C, D + 1):
        if is_prime[t + a]:
            has_prime = True
            break
    if not has_prime:
        winner = "Takahashi"
        break

print(winner)
