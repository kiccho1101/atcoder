N, M = map(int, input().split())

exp_sta = set()

sta = input().split()
for s in input().split():
    exp_sta.add(s)

for s in sta:
    if s in exp_sta:
        print("Yes")
    else:
        print("No")
