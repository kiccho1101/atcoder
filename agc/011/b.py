N = int(input())

A = list(map(int, input().split()))

A.sort()

cumsum = []
for i in range(len(A)):
    if i == 0:
        cumsum.append(A[i])
    else:
        cumsum.append(cumsum[i - 1] + A[i])

ans = 0
cumsum.reverse()
A.reverse()
for i in range(len(cumsum) - 1):
    if A[i] <= cumsum[i + 1] * 2:
        ans += 1
    else:
        break

print(ans + 1)
