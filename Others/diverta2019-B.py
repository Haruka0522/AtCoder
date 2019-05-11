R,G,B,N = map(int,input().split())
ans = 0
RGB = sorted([R,G,B],reverse=True)
R,G,B = RGB[0],RGB[1],RGB[2]
for r in range(int(N/R)+1):
    for g in range(int((N-R*r)/G)+1):
        for b in range(int((N-(R*r+G*g))/B)+1):
            if(R*r+G*g+B*b == N):
                ans += 1
print(ans)

