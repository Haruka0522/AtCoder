N = int(input())
D = list(map(int,input().split()))
ans = 0
for K in range(min(D),max(D)):
    ABC = 0
    for d in D:
        if d < K:
            ABC += 1
    if ABC == N-ABC:
        ans += 1
print(ans)
