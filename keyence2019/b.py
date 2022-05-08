S = input()
n = len(S)

for i in range(n):
    for j in range(0, n - i):
        new_s = S[:i] + S[i + j :]
        if new_s == "keyence":
            print("YES")
            exit()

print("NO")
