import math
n = int(input())
ans = n
for tate in range(1,int(math.sqrt(n))+1):
    yoko = n//tate
    ans = min(ans,(n-tate*yoko)+abs(tate-yoko))
print(ans)
    
