import collections

N = int(input())
A = collections.deque(list(map(int, input().split())))

curr = 0
while A:
    print(A, curr)
    if A[-1] == curr:
        A.pop()
    elif A[0] == curr:
        A.popleft()
        curr = 1 if curr == 0 else 0
    else:
        print("No")
        exit()
print("Yes")
