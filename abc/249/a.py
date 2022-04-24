A, B, C, D, E, F, X = map(int, input().split())

a = 0
j = 0
flag = True
while flag:
    for i in range(A):
        a += B
        j += 1
        if j == X:
            flag = False
            break
    if flag:
        for i in range(C):
            j += 1
            if j == X:
                flag = False
                break

b = 0
j = 0
flag = True
while flag:
    for i in range(D):
        b += E
        j += 1
        if j == X:
            flag = False
            break
    if flag:
        for i in range(F):
            j += 1
            if j == X:
                flag = False
                break

if a > b:
    print("Takahashi")
elif a < b:
    print("Aoki")
else:
    print("Draw")
