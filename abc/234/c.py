K = int(input())

if K == 1:
    exit(print(2))

patterns = 0
keta = 0
while patterns < K:
    patterns += 2 ** keta
    keta += 1

patterns -= 2 ** (keta - 1)
N = K - patterns


b = bin(N - 1)[2:].replace("1", "2")
if len(b) < keta - 1:
    b = "0" * (keta - 1 - len(b)) + b

ans = "2" + b
print(ans)
