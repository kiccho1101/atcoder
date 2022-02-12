# %%
import math


H, W = map(int, input().split())

if H == 1 or W == 1:
    print(H * W)
else:
    h = math.ceil(H / 2)
    w = math.ceil(W / 2)

    print(h * w)
