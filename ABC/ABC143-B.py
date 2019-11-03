N = int(input())
D_list = list(map(int,input().split()))
ans = 0
for i in range(N):
    for j in range(i+1,N):
        ans += D_list[i] * D_list[j]
print(ans)
