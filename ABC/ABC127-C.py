N,M = map(int,input().split())
ans = 0
max_L,min_R = map(int,input().split())
for i in range(M-1):
    L,R = map(int,input().split())
    if max_L < L:
        max_L = L
    if min_R > R:
        min_R = R
print(len([i for i in range(max_L,min_R+1)]))
