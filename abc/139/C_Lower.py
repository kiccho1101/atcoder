import numpy as np

N = input()
a = np.array(input().split()).astype(int)
flags = (np.diff(a) <= 0).astype(int)
result = 0
max_result = 0
for i, flag in enumerate(flags):
    if flag == 0:
        if result > max_result:
            max_result = result
        result = 0
    else:
        result += 1
    if i == len(flags) - 1:
        if result > max_result:
            max_result = result
print(max_result)
