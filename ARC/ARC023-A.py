from math import floor
y = int(input())
m = int(input())
d = int(input())
if m == 1 or m == 2:
    y -= 1
    m = 12 + m
def keikanissuu(y,m,d):
    return 365*y + floor(y/4) - floor(y/100) + floor(y/400) + floor((306*(m+1))/10) + d - 429
print(keikanissuu(2014,5,17) - keikanissuu(y,m,d))
