s = list(input())
K = int(input())

for i in range(len(s)):
    if s[i] == "a":
        continue
    num = ord("z") - ord(s[i]) + 1
    if K >= num:
        s[i] = "a"
        K -= num

if K > 0:
    s[-1] = chr((ord(s[-1]) - ord("a") + K) % 26 + ord("a"))

print("".join(s))
