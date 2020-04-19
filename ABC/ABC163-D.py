from scipy.special import comb
from math import factorial
N,K = map(int,input().split())
ans = 0
mod = 10**9+7
N += 1
a = factorial(N)//factorial(N-K)
j = K
for i in range(K,N+1):
    print(a,j)
    ans += (a//j) % mod
    a *= (N-i)
    j *= (i+1)
print(ans)
