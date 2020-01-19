N = int(input())
P = list(map(int,input().split()))
P_min = [2*(10**5)]
for i in range(N-1):
    P_min.append(min(P_min[i],P[i]))
ans = 0
for i in range(N):
    if P_min[i] >= P[i]:
        ans += 1
print(ans)
