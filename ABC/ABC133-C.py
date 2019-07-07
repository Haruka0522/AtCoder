'''大会中コード
L,R = map(int,input().split())
ans = 2019
for j in range(R+1):
    for i in range(L,j):
        ans = min(ans,(i*j)%2019)
print(ans)
'''

#解説を見て
L,R = map(int,input().split())
ans = 2018
for i in range(L,R):
    for j in range(i+1,R+1):
        ans = min(ans,(i*j)%2019)
        if ans == 0:
            print(0)
            exit()
print(ans)
