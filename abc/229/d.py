S = input()
K = int(input())

ans = 0
right = 0
k = 0
for left in range(len(S)):
    while right < len(S) and (S[right] == "X" or k + 1 <= K):
        if S[right] == ".":
            k += 1
        right += 1

    ans = max(ans, right - left)

    if right == left:
        right += 1
    elif S[left] == ".":
        k -= 1

print(ans)
