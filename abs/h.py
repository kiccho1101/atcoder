N = int(input())

ds = {}
for i in range(N):
    ds[input()] = True

print(len(ds.keys()))
