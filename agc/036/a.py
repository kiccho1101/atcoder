S = int(input())

if S <= 10 ** 9:
    print(0, 0, 0, 1, S, 0)
else:
    q, mod = divmod(S, 10 ** 9)
    if mod != 0:
        q += 1
        mod = 10 ** 9 - mod
    print(0, 0, 1, q, 10 ** 9, mod)
