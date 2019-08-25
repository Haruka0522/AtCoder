M,D = map(int,input().split())
ans = 0
for m in range(1,M+1):
    for d in range(22,D+1):
        d10 = int(str(d)[0])
        d1 = int(str(d)[1])
        if d10 * d1 == m and d1>=2 and d10>=2:
            ans += 1
print(ans)
