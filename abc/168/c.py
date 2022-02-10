import math


A, B, H, M = map(int, input().split())

h = H + M / 60

T_a = 12
T_b = 1

theta_a = 2 * math.pi / T_a * (h % T_a)
theta_b = 2 * math.pi / T_b * (h % T_b)

ax = A * math.cos(theta_a)
ay = A * math.sin(theta_a)

bx = B * math.cos(theta_b)
by = B * math.sin(theta_b)


ans = math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)
print(ans)
