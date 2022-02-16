N, K = map(int, input().split())

MOD = 10 ** 5


idxs = [[] for _ in range(MOD + 1)]


def calc(x):
    return sum(map(int, list(str(x)))) % MOD


while K > 0:
    N = calc(N)
    idxs[N].append(K)
    if len(idxs[N]) >= 2:
        diff = idxs[N][0] - idxs[N][1]
        orig_K = K
        K %= diff
        print(diff, orig_K, K)
    K -= 1

print(N)
