import itertools

n = int(input())
k = int(input())
A = [int(input()) for _ in range(n)]


s = set()
for selected in itertools.permutations(A, k):
    s.add(int("".join(map(str, selected))))

print(len(s))
