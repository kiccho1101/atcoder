n, a, b = list(map(int, input().split()))

result = 0
for i in range(1, n + 1):
    arr = [int(_str) for _str in str(i)]
    s = sum(arr)
    if a <= s <= b:
        result += i
print(result)
