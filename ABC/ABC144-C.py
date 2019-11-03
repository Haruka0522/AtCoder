"""
1   2   3   4   5   6 
2   4   6   8   10  12
3   6   9   12  15  18
4   8   12  16  20  24
5   10  15  20  25  30
"""

import math
N = int(input())
ans = 10**12
root = int(math.sqrt(N))+1
for i in range(1,root):
    if N % i == 0:
        ans = min(ans,(i-1)+(N//i-1))
print(ans)
