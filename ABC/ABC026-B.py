import math
N = int(input())
ans = 0
r_list = []
for i in range(N):
    r_list.append(int(input()))
r_list.sort(reverse=True)
for i in range(len(r_list)):
    if(i%2==0):
        ans += math.pow(r_list[i],2)
    else:
        ans -= math.pow(r_list[i],2)
print(ans*math.pi)
