s = input()

start_i = 0
end_i = len(s) - 1

for i in range(len(s)):
    if s[i] != "a":
        start_i = i
        break
for i in range(len(s) - 1, -1, -1):
    if s[i] != "a":
        end_i = i
        break

ss = "a" * max(0, len(s) - 1 - end_i - start_i) + s
if ss == ss[::-1]:
    print("Yes")
else:
    print("No")
