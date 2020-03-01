N = int(input())
ans = 10**9+7
X_list = list(map(int,input().split()))
for P in range(min(X_list),max(X_list)+1):
    ans = min(ans,sum([(i-P)**2 for i in X_list]))
print(ans)

