N,K = map(int,input().split())
ans = 0
mod = 10**9+7
for k in range(K,N+2):
    ans += (k*(N-k+1)+1)
print(ans % mod)
