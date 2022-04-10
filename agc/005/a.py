S = input()

ans = 0
s_num = 0
for s in S:
    if s == "S":
        s_num += 1
    if s == "T":
        if s_num > 0:
            s_num -= 1
        else:
            ans += 1

print(s_num + ans)
