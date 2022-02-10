a, b = input().split()

a = int(a)

b_int = int(b.replace(".", ""))

ans = a * b_int // 100

print(ans)
