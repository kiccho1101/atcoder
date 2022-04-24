N, K = map(int, input().split())
D = input().split()


def contains(s: str, D):
    for d in D:
        if s.find(d) != -1:
            return True
    return False


while True:
    if not contains(str(N), D):
        print(N)
        exit()
    N += 1
