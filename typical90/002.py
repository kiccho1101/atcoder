# bit全探索の問題

N = int(input())


def check(candidate: str) -> bool:
    num_a = 0
    num_b = 0
    for i in range(len(candidate)):
        if candidate[i] == "(":
            num_a += 1
        if candidate[i] == ")":
            num_b += 1
        if num_a < num_b:
            return False
    return num_a == num_b


for i in range(1 << N):
    candidate = ""
    for j in range(N - 1, -1, -1):
        if i & (1 << j) == 0:
            candidate += "("
        else:
            candidate += ")"
    if check(candidate):
        print(candidate)
