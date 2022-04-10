n = 10 ** 5
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False
for p in range(2, n + 1):
    if is_prime[p]:
        for q in range(2 * p, n + 1, p):
            is_prime[q] = False

cumsum = [0] * (n + 1)
for i in range(1, n + 1):
    cumsum[i] = cumsum[i - 1]
    if i % 2 == 1 and is_prime[i] and is_prime[(i + 1) // 2]:
        cumsum[i] += 1

Q = int(input())
qs = [map(int, input().split()) for _ in range(Q)]
for left, right in qs:
    ans = cumsum[right] - cumsum[left - 1]
    print(ans)
