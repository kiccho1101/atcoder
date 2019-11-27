import numpy as np
import scipy
from scipy.spatial import distance_matrix

N = int(input())

cords = []
for _ in range(N):
    sp = input().split()
    x, y = float(sp[0]), float(sp[1])
    cords.append([x, y])

cords = np.array(cords)
d = distance_matrix(cords, cords)
np.fill_diagonal(d, 0)
print(d.sum() / cords.size * 2)
