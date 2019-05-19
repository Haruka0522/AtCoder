'''自力クソ解答
X,Y = map(int,input().split())
for i in range(1,10**6):
    if((X*i) % Y != 0):
        print(X*i)
        exit()
print(-1)
'''

#良解法
X,Y=map(int,input().split())
print(-1 if X%Y==0 else X)
