T = int(input())

for _ in range(T):
    a, s = map(int, input().split())

    diff = s - 2 * a
    if diff >= 0 and diff & a == 0:
        print("Yes")
    else:
        print("No")
