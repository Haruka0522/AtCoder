N,M = map(int,input().split())
route_list = [0] * N
for i in range(M):
    a,b = map(int,input().split())
    route_list[a-1] += 1
    route_list[b-1] += 1
for ans in route_list:
    print(ans)

