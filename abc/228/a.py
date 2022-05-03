S, T, X = map(int, input().split())

flag = False
while True:
    if S == X:
        flag = True
    S += 1
    S %= 24
    if S == T:
        break

if flag:
    print("Yes")
else:
    print("No")
