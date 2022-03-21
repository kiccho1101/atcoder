def inversion(s):
    ans = 0
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i] > s[j]:
                ans += 1
    return ans % 2


S = input().split()
T = input().split()

if inversion(S) == inversion(T):
    print("Yes")
else:
    print("No")
