N, Y = list(map(int, input().split()))


result_x = -1
result_y = -1
result_z = -1
for x in range(N + 1):
    if 10000 * x > Y:
        break
    for y in range(N - x + 1):
        if 10000 * x - 5000 * y > Y:
            break
        z = (Y - 10000 * x - 5000 * y) / 1000
        if x + y + z == N:
            result_x, result_y, result_z = int(x), int(y), int(z)


print(result_x, result_y, result_z)
