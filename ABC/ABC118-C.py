"""TLE
N = int(input())
HPs = list(map(int,input().split()))
while True:
    min_hp = min(HPs)
    for i in range(len(HPs)):
        if i == HPs.index(min_hp):
            continue
        HPs[i] = HPs[i] % min_hp
    tmp = HPs.count(0)
    for j in range(tmp):
        if tmp==len(HPs):
            print(HPs[0])
            exit()
        HPs.remove(0)
    if len(HPs)==1:
        break
print(HPs[0])
"""
from fractions import gcd
N = int(input())
HPs = list(map(int,input().split()))
ans = HPs[0]
for i in HPs:
    ans = gcd(ans,i)
print(ans)
