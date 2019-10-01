N,K = map(int,input().split())
hight = list(map(int,input().split()))
ans = 0
for i in hight:
    if i >= K:
        ans += 1
print(ans)
