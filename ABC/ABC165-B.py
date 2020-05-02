from math import log,ceil
X = int(input())
i = 100
cnt = 0
while True:
    i *= 1.01
    i = int(i)
    cnt += 1
    if i >= X:
        break

print(cnt)
