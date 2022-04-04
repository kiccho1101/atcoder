s = input()
s_without_x = s.replace("x", "")

if s_without_x != s_without_x[::-1]:
    print(-1)
    exit()

x_nums_left = []
idx = 0
while idx < len(s):
    num = 0
    while idx < len(s) and s[idx] == "x":
        num += 1
        idx += 1
    x_nums_left.append(num)
    idx += 1

s_rev = s[::-1]
x_nums_right = []
idx = 0
while idx < len(s_rev):
    num = 0
    while idx < len(s_rev) and s_rev[idx] == "x":
        num += 1
        idx += 1
    x_nums_right.append(num)
    idx += 1

ans = 0
s_len = len(s_without_x)
n = s_len // 2 if s_len % 2 == 0 else s_len // 2 + 1
for i in range(n):
    ans += abs(x_nums_left[i] - x_nums_right[i])

print(ans)
