S = input()

S = S.replace("BC", "X")

cnt = 0
ans = 0

for s in reversed(S):
    if s == "A":
        ans += cnt
    elif s == "X":
        cnt += 1
    else:
        cnt = 0
print(ans)
