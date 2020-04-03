n,X = map(int,input().split())
a_li = list(map(int,input().split()))
X_bin = bin(X)
ans = 0
for k in range(n):
    if X >> k & 1:
        ans += a_li[k]
print(ans)
