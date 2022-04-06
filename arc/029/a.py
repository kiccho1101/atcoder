N = int(input())
ts = [int(input()) for _ in range(N)]

ts.sort()

t_1 = 0
t_2 = 0
while ts:
    t = ts.pop()
    if t_1 > t_2:
        t_2 += t
    else:
        t_1 += t

print(max(t_1, t_2))
