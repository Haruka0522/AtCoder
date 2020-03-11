import math
A,B = map(int,input().split())
ans = []
for i in range(1,1300):
    if math.floor(i * 0.08) == A and math.floor(i * 0.10) == B:
        ans.append(i)
if ans == []:
    print(-1)
else:
    print(min(ans))
