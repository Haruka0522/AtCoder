from math import gcd
ans = 0
K = int(input())
for i in range(1,K+1):
    for j in range(1,K+1):
        a = gcd(i,j)
        for k in range(1,K+1):
            ans += gcd(a,k)
print(ans)
