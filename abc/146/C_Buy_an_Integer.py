import numpy as np

A, B, X = np.array(input().split()).astype(int).tolist()

flag = 1
upper = 10 ** 9
lower = 0

if A * upper + B * (int(np.log10(upper)) + 1) <= X:
    result = upper
    flag = 0

while flag == 1:

    m = int((upper + lower) / 2)

    if A * m + B * (int(np.log10(m)) + 1) > X:
        upper = m
    else:
        lower = m

    if lower + 1 == upper:
        result = lower
        flag = 0

print(result)
