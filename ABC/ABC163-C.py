N = int(input())
ans = [0]*N
A_list = list(map(int,input().split()))
for i in A_list:
    ans[i-1] += 1
for i in ans:
    print(i)

