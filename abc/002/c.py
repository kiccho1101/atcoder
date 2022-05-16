xa, ya, xb, yb, xc, yc = map(int, input().split())

xb -= xa
xc -= xa

yb -= ya
yc -= ya

ans = abs(xb * yc - xc * yb) / 2
print(ans)
