#TLE解法
"""
N = int(input())
H_list = list(map(int,input().split()))
ans = 0
for i in range(N):
    a = 0
    oritatokoro = H_list[i]
    for j in range(i+1,N-1):
        if H_list[j] >= H_list[j+1]:
            a += 1
        else:
            break
    if ans < a:
        ans = a
print(ans)
"""
