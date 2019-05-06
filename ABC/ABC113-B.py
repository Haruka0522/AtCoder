N = int(input())
T,A = map(int,input().split())
Heights = list(map(int,input().split()))
sa_list = []
for i in Heights:
    temp = T-i*0.006
    sa = abs(A-temp)
    sa_list.append(sa)
print(sa_list.index(min(sa_list))+1)