N,M = map(int,input().split())
H_li = list(map(int,input().split()))
ans = 0
route = [[] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    route[a].append(b)
    route[b].append(a)
for i in range(N):
    i_h = H_li[i]
    ikeru = route[i]
    if ikeru == []:
        ans += 1
        continue
    ikeru_h = [H_li[j] for j in ikeru]
    if max(ikeru_h) < i_h:
        ans += 1
print(ans)



