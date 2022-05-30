N = int(input())
A = list(map(int, input().split()))

nums = [0] * 3

for a in A:
    if a % 4 == 0:
        nums[2] += 1
    elif a % 2 == 0:
        nums[1] += 1
    else:
        nums[0] += 1

ans = "Yes"
if nums[1] >= 2:
    if nums[0] > nums[2]:
        ans = "No"
else:
    if nums[0] + nums[1] > nums[2] + 1:
        ans = "No"

print(ans)
