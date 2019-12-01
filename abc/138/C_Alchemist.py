import numpy as np

N = input()
a = np.array(input().split()).astype(int)
a = np.sort(a)
print(
    (
        np.power(2, np.arange(len(a)) - np.insert(np.ones(len(a) - 1), 0, 0))
        * a
        / np.power(2, len(a) - 1)
    ).sum()
)
