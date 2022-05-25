N = int(input())
A = list(map(int, input().split()))

ans = set()
for a in A:
    while a % 2 == 0:
        a //= 2
    ans.add(a)


print(len(ans))
