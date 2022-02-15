N = int(input())

MOD = 46

A_num = [0] * MOD
B_num = [0] * MOD
C_num = [0] * MOD

for i in list(map(int, input().split())):
    i %= MOD
    A_num[i] += 1
for i in list(map(int, input().split())):
    i %= MOD
    B_num[i] += 1
for i in list(map(int, input().split())):
    i %= MOD
    C_num[i] += 1

ans = 0

for a in range(MOD):
    for b in range(MOD):
        for c in range(MOD):
            if (a + b + c) % MOD == 0:
                ans += A_num[a] * B_num[b] * C_num[c]

print(ans)
