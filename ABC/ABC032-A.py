import math
a = int(input())
b = int(input())
n = int(input())
lcm = a*b/math.gcd(a,b)
cm = lcm
while(cm < n):
    cm = cm + lcm
print(int(cm))