a,b,t = map(int,input().split())
ans = 0
for i in range(1,100):
    if(i*a > t+0.5):
        break
    ans += b
print(ans)

