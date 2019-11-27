import numpy as np
from operator import itemgetter

N = input()
a = np.array(input().split()).astype(int)
print(
    " ".join(
        np.array(
            sorted(
                np.array([a, np.arange(1, len(a) + 1)]).T.tolist(),
                key=itemgetter(0),
                reverse=False,
            )
        )
        .T[1]
        .astype(str)
    )
)
