N = int(input())

flag = "No"
for i in range(1, 10):
    for j in range(i, 10):
        if i * j == N:
            flag = "Yes"
            break
print(flag)
