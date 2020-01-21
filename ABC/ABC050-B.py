N = int(input())
T_list = list(map(int,input().split()))
M = int(input())
for i in range(M):
    P,X = map(int,input().split())
    ans = T_list.copy()
    ans[P-1] = X
    print(sum(ans))

