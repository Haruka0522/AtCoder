N = int(input())
v_list = sorted(list(map(int,input().split())))
for i in range(N-1):
    if i == 0:
        ans = (v_list[i]+v_list[i+1])/2
    else:
        ans = (ans+v_list[i+1])/2
print(ans)
