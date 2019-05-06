import math
x1, y1, x2, y2 = map(int, input().split())
ippen = math.sqrt((y2 - y1) ** 2 + (x2 - x1)**2)
taikakusen = math.sqrt(ippen ** 2)
x3 = taikakusen ** 2 - x1 ** 2
y3 = taikakusen ** 2 - y1 ** 2
x4 = taikakusen ** 2 - x2 ** 2
y4 = taikakusen ** 2 - y2 ** 2
print(x3, y3, x4, y4)
