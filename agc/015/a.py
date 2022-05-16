N, A, B = map(int, input().split())

if A > B:
    print(0)
    exit()

if N == 1:
    if A == B:
        print(1)
    else:
        print(0)
    exit()

lower = A * (N - 1) + B
upper = B * (N - 1) + A
print(upper - lower + 1)
