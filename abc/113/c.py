import sys

input = sys.stdin.readline

N, M = map(int, input().split())

prefs = {}

for i in range(M):
    pref, year = map(int, input().split())
    if pref not in prefs:
        prefs[pref] = []
    prefs[pref].append((year, i))

for pref in prefs.keys():
    prefs[pref].sort()

output = {}
for pref in prefs.keys():
    prefix = str(pref).zfill(6)
    for i in range(len(prefs[pref])):
        postfix = str(i + 1).zfill(6)
        output[prefs[pref][i][1]] = f"{prefix}{postfix}"

for i in range(M):
    print(output[i])
