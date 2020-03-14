from math import sqrt
a,b,c = map(int,input().split())
if sqrt(a) + sqrt(b) <sqrt(c):
    print("Yes")
else:
    print("No")

