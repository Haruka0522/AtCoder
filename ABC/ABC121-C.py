N,M = map(int,input().split())
AB = []
for i in range(N):
    A,B = map(int,input().split())
    AB.append((A,B))
AB.sort()
cnt = 0
ans = 0
for a,b in AB:
    if cnt+b >= M:
        break
    cnt += b
    ans += a*b
ans += a*(M-cnt)
print(ans)
