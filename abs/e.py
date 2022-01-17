A = int(input())
B = int(input())
C = int(input())

X = int(input())

result = 0
for a in range(A + 1):
    if 500 * a > X:
        break
    for b in range(B + 1):
        if 500 * a + 100 * b > X:
            break
        for c in range(C + 1):
            s = 500 * a + 100 * b + 50 * c
            if s > X:
                break
            if s == X:
                result += 1
print(result)
