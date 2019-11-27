N = int(input())
S = input()
result = ""
previous = ""
for s in S:
    if s != previous:
        result += s
    previous = s
print(len(result))
