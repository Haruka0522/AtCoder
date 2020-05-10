from itertools import combinations
import numpy as np
N,M,X = map(int,input().split())
setto = list(range(N))
ans = 10**18
sankosyo = [list(map(int,input().split())) for i in range(N)]
subsets = []
for i in range(N+1):
    for c in combinations(setto,i):
        subsets.append(c)
for subset in subsets:
    cost = 0
    rikaido = np.array([0]*M)
    if subset == set():
        continue
    for i in subset:
        cost += sankosyo[i][0]
        for idx,A in enumerate(sankosyo[i][1:]):
            rikaido[idx] += A
    if np.count_nonzero(rikaido < X) == 0:
        ans = min(ans,cost)
if ans == 10**18:
    print(-1)
else:
    print(ans)
