from math import sqrt

n = int(input())
x_list = list(map(int, input().split()))
m, e, c = 0, 0, 0
for x in x_list:
    m += abs(x)
    e += x ** 2
    c = max(abs(x), c)

print(m)
print(sqrt(e))
print(c)
