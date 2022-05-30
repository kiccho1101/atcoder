s = list(input())
t = list(input())


if "".join(sorted(s)) < "".join(sorted(t, reverse=True)):
    print("Yes")
else:
    print("No")
