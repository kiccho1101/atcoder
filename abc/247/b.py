import collections

N = int(input())
names = collections.defaultdict(int)
st = [input().split() for _ in range(N)]

for s, t in st:
    names[s] += 1
    names[t] += 1


for s, t in st:
    names[s] -= 1
    names[t] -= 1
    if names[s] > 0 and names[t] > 0:
        print("No")
        exit()
    names[s] += 1
    names[t] += 1

print("Yes")
