A,B,M = map(int,input().split())
a_li = list(map(int,input().split()))
b_li = list(map(int,input().split()))
ans = min(a_li) + min(b_li)
for i in range(M):
    x,y,c = map(int,input().split())
    ans = min(ans, a_li[x-1] + b_li[y-1] - c)
print(ans)
