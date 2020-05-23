import numpy as np
N,M,Q = map(int,input().split())
graph = np.array([[0]*N for _ in range(N)])
ans = []
for _ in range(M):
    u,v = map(int,input().split())
    graph[u-1,v-1] = 1
    graph[v-1,u-1] = 1
color = np.array(list(map(int,input().split())))
for i in range(Q):
    s = list(map(int,input().split()))
    if s[0] == 1:
        x = s[1] - 1
        x_color = color[x]
        ans.append(x_color)
        mask = np.array(graph[x],dtype=bool)
        color[mask] = x_color
    else:
        x,y = s[1] - 1,s[2]
        x_color = color[x]
        ans.append(x_color)
        color[x] = y
for i in ans:
    print(i)
