S = input()
result = 0
for i in range(int(len(S) / 2)):
    if S[i] != S[-(i + 1)]:
        result += 1
print(result)
