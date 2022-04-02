import math


a, b = map(int, input().split())

dist = math.sqrt(a ** 2 + b ** 2)

print(a / dist, b / dist)
