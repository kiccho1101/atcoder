import math


X, Y = map(int, input().split())

ans = math.ceil((Y - X) / 10.0)
if ans <= 0:
    print(0)
else:
    print(ans)
