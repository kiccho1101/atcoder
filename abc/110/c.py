S = input()
T = input()

chars = [[0] * 26 for _ in range(26)]

for i in range(len(S)):
    s = ord(S[i]) - ord("a")
    t = ord(T[i]) - ord("a")

    chars[s][t] = 1

for i in range(26):
    num = 0
    for j in range(26):
        if chars[i][j] == 1:
            num += 1
    if num > 1:
        print("No")
        exit()

for j in range(26):
    num = 0
    for i in range(26):
        if chars[i][j] == 1:
            num += 1
    if num > 1:
        print("No")
        exit()
print("Yes")
