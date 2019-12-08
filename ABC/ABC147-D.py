N = int(input())
A_list = list(map(int,input().split()))
ans = 0
for i in range(N-1):
    for j in range(i+1,N):
        ans += (A_list[i] ^ A_list[j])
print(ans%(10**9+7))
