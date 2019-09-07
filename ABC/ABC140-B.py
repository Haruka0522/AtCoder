N = int(input())
A_list = list(map(int,input().split()))
B_list = list(map(int,input().split()))
C_list = list(map(int,input().split()))
ans = 0
for i in range(N):
    ans += B_list[A_list[i]-1]
    
    if i < N-1:
        if A_list[i]+1==A_list[i+1]:
            ans += C_list[A_list[i]-1]
print(ans)
