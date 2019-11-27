A_str, B_str = input().split()
A, B = int(A_str), int(B_str)

if 1 <= A <= 9 and 1 <= B <= 9:
    print(A * B)
else:
    print(-1)
