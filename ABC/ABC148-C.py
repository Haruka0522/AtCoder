#from math import gcd
from fractions import gcd
A,B = map(int,input().split())

#最小公倍数
def lcm(x,y):
    return (x*y//gcd(x,y))

print(lcm(A,B))
