N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans = 0
for i in range(N):
    taosu_i = min(A[i],B[i])
    ans += taosu_i
    taosu_i2 = B[i]-taosu_i
    A[i+1] = max(A[i+1]-taosu_i2,0)
print(ans)
