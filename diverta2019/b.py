R, G, B, N = map(int, input().split())

ans = 0
for r in range(3001):
    if r * R > N:
        break
    for g in range(3001):
        if r * R + g * G > N:
            break
        b = (N - r * R - g * G) / B
        if b.is_integer():
            ans += 1

print(ans)
