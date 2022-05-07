S = list(input())

B = 0
ans = 0

for s in S:
    if s == "B":
        B += 1
    else:
        ans += B

print(ans)
