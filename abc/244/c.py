N = int(input())

remaining = set(range(1, 2 * N + 2))

while True:
    print(remaining.pop(), flush=True)

    takahashi = int(input())
    if takahashi == 0:
        exit()
    remaining.remove(takahashi)
