#TLE
import math
n,a,b = map(int,input().split())
ans = 0
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
for i in range(1,n+1):
    if i == a or i == b:
        continue
    else:
        ans += combinations_count(n,i)%(10**9+7)
print(ans)
