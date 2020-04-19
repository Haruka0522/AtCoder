N,M = map(int,input().split())
A_li = list(map(int,input().split()))
print(max(N-sum(A_li),-1))
