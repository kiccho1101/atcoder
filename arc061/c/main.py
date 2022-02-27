from itertools import product

S = input()

N = len(S) - 1


ans = 0
for bit in product((0, 1), repeat=N):
    s = S[0]
    for i, b in enumerate(bit):
        if b == 1:
            ans += int(s)
            s = ""
        s += S[i + 1]
    ans += int(s)


print(ans)
