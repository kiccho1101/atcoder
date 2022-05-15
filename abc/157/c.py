N, M = map(int, input().split())

specs = {}
for _ in range(M):
    s, c = map(int, input().split())
    if s in specs and specs[s] != c:
        print(-1)
        exit()
    specs[s] = c

for i in range(0, 1000):
    i_str = str(i)
    if len(i_str) == N:
        flag = True
        for s, c in specs.items():
            if i_str[s - 1] != str(c):
                flag = False

        if flag:
            print(i)
            exit()

print(-1)
