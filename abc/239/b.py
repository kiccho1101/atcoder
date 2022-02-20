X = input()

if len(X) == 1:
    exit(print(0))
elif len(X) == 2 and X[0] == "-":
    exit(print(-1))

x = int(X[:-1])
last_digit = X[-1]


if last_digit == "0":
    print(x)
else:
    if x < 0:
        print(x - 1)
    else:
        print(x)
