import numpy as np
from scipy.sparse.csgraph import shortest_path
from scipy.sparse import csr_matrix
N,X,Y = map(int,input().split())

#隣接リストの整備
"""
route_list = np.zeros((N,N))
route_list[0][1] = 1
for i in range(1,N-1):
    route_list[i][i-1] = 1
    route_list[i][i+1] = 1
print(route_list)
route_list[-1][-2] = 1
route_list[X-1][Y-1] = 1
route_list[Y-1][X-1] = 1
"""
a = np.ones(N-1)
route_list = np.diag(a,k=1)
#b = np.diag(a,k=1)
#c = np.diag(a,k=-1)
#route_list = b | c
route_list[X-1][Y-1] = 1
route_list[Y-1][X-1] = 1

shortest = shortest_path(route_list,directed=False,method="D")

for i in range(1,N):
    print(np.count_nonzero(shortest == i)//2)
