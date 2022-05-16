S = input()
T = input()

if len(S) != len(T):
    print("You will lose")
    exit()

for i in range(len(S)):
    if S[i] == T[i] == "@":
        continue
    elif S[i] == "@":
        if T[i] not in "atcoder":
            print("You will lose")
            exit()
    elif T[i] == "@":
        if S[i] not in "atcoder":
            print("You will lose")
            exit()
    else:
        if S[i] != T[i]:
            print("You will lose")
            exit()

print("You can win")
