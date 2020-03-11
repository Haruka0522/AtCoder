N = int(input())
ans = 10**9+7
for A in range(1,N//2+2):
    B = N - A
    A_ = [int(i) for i in list(str(A))]
    B_ = [int(i) for i in list(str(B))]
    ans = min(ans,sum(A_)+sum(B_))
print(ans)
