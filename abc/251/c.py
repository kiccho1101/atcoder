N = int(input())
st = [input().split() for _ in range(N)]

db = {}

for i, (s, t) in enumerate(st):
    if s not in db:
        db[s] = (i, int(t))

max_i = -1
max_t = -1
for i, t in db.values():
    if max_t < t:
        max_t = t
        max_i = i

print(max_i + 1)
