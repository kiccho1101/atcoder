N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

A_rows = []
X_exists = False
Y_exists = False
A_tmp = []
for i, a in enumerate(A):
    if a == X:
        X_exists = True
    if a == Y:
        Y_exists = True

    if Y <= a <= X:
        A_tmp.append(a)
        if i == len(A) - 1 and X_exists and Y_exists:
            A_rows.append(A_tmp)
    else:
        if X_exists and Y_exists:
            A_rows.append(A_tmp)
        X_exists = False
        Y_exists = False
        A_tmp = []


ans = 0
for row in A_rows:
    N = len(row)
    X_count = 0
    Y_count = 0
    right = 0
    for left in range(N):
        while right < N and (X_count == 0 or Y_count == 0):
            if row[right] == X:
                X_count += 1
            if row[right] == Y:
                Y_count += 1
            right += 1

        if X_count > 0 and Y_count > 0:
            ans += N - right + 1

        if right == left:
            right += 1
        else:
            if row[left] == X:
                X_count -= 1
            if row[left] == Y:
                Y_count -= 1

print(ans)
