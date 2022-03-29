N = int(input())
A = list(map(int, input().split()))

minus_count = 0
zero_count = 0
abs_min = float("inf")
for i in range(len(A)):
    if A[i] == 0:
        zero_count += 1
    if A[i] < 0:
        minus_count += 1
    A[i] = abs(A[i])
    abs_min = min(abs_min, A[i])

if zero_count > 1 or minus_count % 2 == 0:
    print(sum(A))
else:
    print(sum(A) - 2 * abs_min)
