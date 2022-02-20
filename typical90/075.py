import math
import numpy as np


def factorization(n):
    result = []
    while n % 2 == 0:
        result.append(2)
        n //= 2

    f = 3
    while f * f <= n:
        if n % f == 0:
            result.append(f)
            n //= f
        else:
            f += 2

    if n != 1:
        result.append(n)

    return result


print(math.ceil(np.log2(len(factorization(int(input()))))))
