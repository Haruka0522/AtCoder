N,K = map(int,input().split())
ans = [0] * N
for _ in range(K):
    d = int(input())
    A_li = list(map(int,input().split()))
    for i in A_li:
        ans[i-1] = 1
print(ans.count(0))
