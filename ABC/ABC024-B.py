N,T = map(int,input().split())
N_li = [int(input()) for i in range(N)]
flag = False
ans = T
for i in range(1,N):
    if N_li[i-1] + T > N_li[i]:
        ans += N_li[i] - N_li[i-1]
    else:
        ans += T
print(ans)
