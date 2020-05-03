N,K = map(int,input().split())
num = [0]*(10**5+1)
for i in range(N):
    a,b = map(int,input().split())
    num[a] += b
for i in range(1,10**5+1):
    if K <= num[i]:
        print(i)
        exit()
    K -= num[i]
