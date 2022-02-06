_ = input()

A = list(map(int, input().split()))

s = 0
part_s = 0
max_part_s = 0
ans = 0
for a in A:
    part_s += a
    max_part_s = max(max_part_s, part_s)
    ans = max(ans, s + max_part_s)
    s += part_s
print(ans)
