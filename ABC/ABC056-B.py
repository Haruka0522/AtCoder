W,a,b = map(int,input().split())
ans = max(b - (a + W),a - (b + W))
if ans <= 0:
    print(0)
else:
    print(ans)
