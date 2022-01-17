a, b = input().split()

a_int = int(a)
b_int = int(b)

product = a_int * b_int

if product % 2 == 0:
    print("Even")
else:
    print("Odd")
