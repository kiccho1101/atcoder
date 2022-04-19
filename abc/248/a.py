S = input()

exists = [False] * 10
for s in S:
    exists[int(s)] = True

for i in range(10):
    if not exists[i]:
        print(i)
        exit()
