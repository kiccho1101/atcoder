N = int(input())

nums = set()

for _ in range(N):
    a = int(input())
    if a in nums:
        nums.remove(a)
    else:
        nums.add(a)

print(len(nums))
