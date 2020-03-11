N,A,B = map(int,input().split())
ans = 0
ans += (N//(A+B)) * A
i = min((N % (A+B)),A)
if i >= 0:
    ans += i
print(ans)
