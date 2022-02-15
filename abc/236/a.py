S = input()

a, b = map(int, input().split())

a -= 1
b -= 1

aa = S[a]
bb = S[b]


ans = ""
for i in range(len(S)):
    if i == a:
        ans += bb
    elif i == b:
        ans += aa
    else:
        ans += S[i]


print(ans)
