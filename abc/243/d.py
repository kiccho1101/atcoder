N, X = map(int, input().split())
S = input()

T = []
for s in S:
    if s == "U" and len(T) > 0 and (T[-1] == "L" or T[-1] == "R"):
        T.pop()
    else:
        T.append(s)

for s in T:
    if s == "U":
        X = X // 2
    if s == "L":
        X = 2 * X
    if s == "R":
        X = 2 * X + 1

print(X)
