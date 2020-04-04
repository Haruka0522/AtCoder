N,M = map(int,input().split())
A_li = list(map(int,input().split()))
cnt = 0
lim = (1 / (4*M)) * sum(A_li)
for i in A_li:
    if i >= lim:
        cnt += 1
if cnt >= M:
    print("Yes")
else:
    print("No")

