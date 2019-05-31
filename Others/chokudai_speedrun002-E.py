ans = 0
for i in range(int(input())):
    a,b = map(int,input().split())
    ans += min(a//2,b)
print(ans)

