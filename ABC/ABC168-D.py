import numpy as np
from scipy.sparse.csgraph import shortest_path
N,M = map(int,input().split())
graph = np.zeros((N,N),dtype=int)
for _ in range(M):
    A,B = map(int,input().split())
    A,B = A-1,B-1
    graph[A,B] = 1
    graph[B,A] = 1
print("Yes")
for i in range(1,N):
    d,p = shortest_path(graph,directed=False,return_predecessors=True)
    print(p[0][i]+1)
