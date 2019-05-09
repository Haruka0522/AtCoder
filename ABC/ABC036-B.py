N = int(input())
S_list = []
ans = []
for i in range(N):
    S_list.append(list(input()))
for i in range(N):
    for j in range(N):
        ans.append(S_list[N-j-1][i])
count = 0
for i in ans:
    if(count == N-1):
        print(i)
        count = 0
    else:
        print(i,end="")
        count += 1
