L,R = map(int,input().split())
ans = 2019
for j in range(R+1):
    for i in range(L,j):
        ans = min(ans,(i*j)%2019)
print(ans)
