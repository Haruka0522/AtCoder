N,K = map(int,input().split())
ans = 0
for i in range(1,N+1):
    t = 0
    while i < K:
        i *= 2
        t += 1
    ans += (1/2) ** t
print((1/N)*ans)
