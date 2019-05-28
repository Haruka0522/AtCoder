N = int(input())
ans = int(input())

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

def lcm(x,y):
    return (x*y//gcd(x,y))

for i in range(N-1):
    t = int(input())
    ans = lcm(ans,t) 

print(ans)
