N = int(input())
K = int(input())
x_li = list(map(int,input().split()))
ans = 0
for i in range(N):
    ans += min(2*x_li[i],2*(abs(K-x_li[i])))
print(ans)
