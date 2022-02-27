from itertools import product

A = list(map(int, list(input())))

N = len(A) - 1

for bits in product((0, 1), repeat=N):
    s = A[0]
    s_str = f"{A[0]}"
    for i, b in enumerate(bits):
        if b == 1:
            s += A[i + 1]
            s_str += f"+{A[i+1]}"
        else:
            s -= A[i + 1]
            s_str += f"-{A[i+1]}"

    if s == 7:
        s_str += "=7"
        print(s_str)
        exit()
