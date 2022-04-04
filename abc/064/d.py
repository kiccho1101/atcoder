N = int(input())
S = input()

ans_left_num = 0
left_num = 0
right_num = 0
for s in S:
    if s == "(":
        left_num += 1
    if s == ")":
        right_num += 1
    if right_num - left_num > 0:
        ans_left_num = max(ans_left_num, right_num - left_num)

ans_right_num = 0
left_num = 0
right_num = 0
for s in reversed(S):
    if s == "(":
        left_num += 1
    if s == ")":
        right_num += 1
    if left_num - right_num > 0:
        ans_right_num = max(ans_right_num, left_num - right_num)

ans = "(" * ans_left_num + S + ")" * ans_right_num
print(ans)
