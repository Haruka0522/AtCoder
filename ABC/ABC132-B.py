N = int(input())
P = list(map(int,input().split()))
ans = 0
for i in range(N-2):
    p = P[i:i+3]
    if min(p)!=p[1] and max(p)!=p[1]:
        ans += 1
print(ans)
