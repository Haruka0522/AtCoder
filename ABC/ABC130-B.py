N,X = map(int,input().split())
ans = 0
L_list =[0]+list(map(int,input().split()))
D = 0
for i in L_list:
    D += i
    if D <= X:
        ans += 1
print(ans)
