N,K,M = map(int,input().split())
A_list = list(map(int,input().split()))
ans = M*N - sum(A_list)
if ans > K:
    print(-1)
elif ans <= 0:
    print(0)
else:
    print(ans)
