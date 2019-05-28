import fractions
N = int(input())
ans = 1

def lcm(x,y):
    return (int(x*y/fractions.gcd(x,y)))

for i in range(N):
    ans = lcm(ans,int(input()))

print(ans)
