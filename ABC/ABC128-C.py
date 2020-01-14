N,M = map(int,input().split())
bin_list = []
ans = 0
for i in range((N)**2):
    bin_list = [0] * N
    for j in range(N):
        if i>>j & 1:
            bin_list[j] = 1

    
