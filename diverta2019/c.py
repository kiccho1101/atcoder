N = int(input())

s_dict = {"A": 0, "B": 0, "AB": 0}

ans = 0
for _ in range(N):
    s = input()
    for i in range(len(s) - 1):
        if s[i : i + 2] == "AB":
            ans += 1
    if s.endswith("A") and s.startswith("B"):
        s_dict["AB"] += 1
    elif s.endswith("A"):
        s_dict["A"] += 1
    elif s.startswith("B"):
        s_dict["B"] += 1

if s_dict["AB"] >= 1:
    ans += s_dict["AB"] - 1
    if s_dict["A"] >= 1:
        ans += 1
        s_dict["A"] -= 1
    if s_dict["B"] >= 1:
        ans += 1
        s_dict["B"] -= 1

ans += min(s_dict["A"], s_dict["B"])
print(ans)
