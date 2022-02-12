N, K = map(int, input().split())

if K == 1:
    print(N - 1)
    exit()

is_prime = [True] * (N + 1)
prime_num = [0] * (N + 1)
for i in range(2, N + 1):
    if is_prime[i]:
        for j in range(i, N + 1, i):
            is_prime[j] = False
            prime_num[j] += 1


ans = 0
for i in range(1, N + 1):
    if prime_num[i] >= K:
        ans += 1

print(ans)
