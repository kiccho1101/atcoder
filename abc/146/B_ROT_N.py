N = int(input())
S = input()
result = ""
for i in range(len(S)):
    diff = ord(S[i]) + N
    if diff > 90:
        diff -= 90
        diff += 64
    result += chr(diff)
print(result)
