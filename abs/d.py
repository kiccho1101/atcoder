_ = input()

numbers = list(map(int, input().split()))

result = 0
flag = True
while flag:
    for i in range(len(numbers)):
        if numbers[i] % 2 != 0:
            flag = False
            break
        numbers[i] = numbers[i] / 2
    if flag:
        result += 1

print(result)
