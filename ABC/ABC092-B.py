N = int(input())
D,X = map(int,input().split())
ans = 0
for i in range(N):
    A = int(input())
    sankasya_i = 0
    j = 0
    while(True):
        day = A*j+1
        j+=1
        if(day > D):
            break
        sankasya_i += 1
    ans += sankasya_i
print(ans+X)
