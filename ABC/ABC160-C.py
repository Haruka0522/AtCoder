K,N = map(int,input().split())
A_list = list(map(int,input().split()))
sa = []
for i in range(1,N):
    sa.append(abs(A_list[i]-A_list[i-1]))
sa.append(K-A_list[-1] + A_list[0])
print(sum(sa)-max(sa))
