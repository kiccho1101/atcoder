A_str, B_str = input().split()
A, B = int(A_str), int(B_str)
ans = A - B * 2
if ans < 0:
    print(0)
else:
    print(ans)
