S = list(input())
T = list(input())


if len(S) == 1:
    print("Yes")
    exit()


def get_diff(s, t):
    if ord(t) >= ord(s):
        return ord(t) - ord(s)
    else:
        return ord("z") - ord(s) + ord(t) - ord("a") + 1


diff = get_diff(S[0], T[0])
for i in range(1, len(S)):
    o = ord(S[i]) + diff
    if o > ord("z"):
        o = o - ord("z") + ord("a") - 1
    if chr(o) != T[i]:
        print("No")
        exit()

print("Yes")
