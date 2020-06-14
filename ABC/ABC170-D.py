N = int(input())
A_li_org = list(map(int,input().split()))
A_li = sorted(list(set(A_li_org)))
tisai = []
ans = 0
flag = False
for i in A_li:
    for j in tisai:
        if i % j == 0:
            flag = True
            break
    tisai.append(i)
    if not flag:
        ans += 1
    flag = False
if len(A_li) == 1:
    print(0)
else:
    print(ans)
