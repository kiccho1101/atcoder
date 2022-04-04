N = int(input())
S = input()

b, w = 0, S.count(".")

ans = w
for i in range(len(S)):
    if S[i] == "#":
        b += 1
    else:
        w -= 1
    ans = min(ans, b + w)

print(ans)
