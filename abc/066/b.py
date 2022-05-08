S = input()

while len(S) > 0:
    S = S[:-1]
    n = len(S)
    if n % 2 == 0 and S[: n // 2] == S[n // 2 :]:
        print(n)
        exit()

print(0)
