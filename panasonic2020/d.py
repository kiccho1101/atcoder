N = int(input())


ans = []


def dfs(s="a"):
    if len(s) == N:
        ans.append(s)
        return

    for i in range(ord("a"), max(map(ord, s)) + 2):
        c = chr(i)
        dfs(s + c)


dfs()
print(*ans, sep="\n")
