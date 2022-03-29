from collections import defaultdict
import sys

input = sys.stdin.readline

MOD = 998244353
N = int(input())
D = list(map(int, input().split()))

if D.pop(0) != 0:
    print(0)
    exit()
if 0 in D:
    print(0)
    exit()

num_count = defaultdict(int)
for i in range(len(D)):
    num_count[D[i]] += 1

num_count[0] = 1
ans = 1
max_dist = max(num_count.keys())
for i in range(1, max_dist + 1):
    ans *= pow(num_count[i - 1], num_count[i])
    ans %= MOD

print(ans)
