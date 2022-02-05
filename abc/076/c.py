S = input()
T = input()


def hantei(ss, T):
    if len(ss) != len(T):
        return False
    for i in range(len(ss)):
        if ss[i] != T[i] and ss[i] != "?":
            return False
    return True


t_idx = -1
for i, s in enumerate(S):
    if hantei(S[i : (i + len(T))], T):
        t_idx = i

if t_idx == -1:
    print("UNRESTORABLE")
else:
    ans = ""
    for i in range(len(S)):
        if t_idx <= i < t_idx + len(T):
            ans += T[i - t_idx]
        else:
            ans += S[i]
    print(ans.replace("?", "a"))
