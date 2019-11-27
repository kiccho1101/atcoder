import numpy as np

S = input()
result = ["No", "Yes"]
print(
    result[
        np.array(
            [
                s in list("RUD") if i % 2 == 0 else s in list("LUD")
                for i, s in enumerate(S)
            ]
        )
        .all()
        .astype(int)
    ]
)
