N = int(input())
S = input()
T = input()

idx = N
for i in range(N):
    if S[i:] == T[: N - i]:
        idx = i
        break


print(N + idx)
