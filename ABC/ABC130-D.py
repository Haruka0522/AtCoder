import numpy as np
N,K = map(int,input().split())
a_list = list(map(int,input().split()))
a_cumsum_ = np.cumsum(a_list)
a_cumsum = np.insert(a_cumsum_,0,0)
ans = 0
for i in range(N+1):
    for j in range(i):
        if(a_cumsum[i]-a_cumsum[j] >= K):
            ans += 1
print(ans)
