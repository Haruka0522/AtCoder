N,M,Q = map(int,input().split())
ans_li = []
abcd = [tuple(map(int,input().split())) for _ in range(Q)]
max_lim = sum([i[3] for i in abcd])
for n in range(10**N):
    ans = 0
    if len(str(n)) != N:
        continue
    A = list(str(n))
    for a,b,c,d in abcd:
        if int(A[b-1]) - int(A[a-1]) == c:
            ans += d
    ans_li.append(ans)
    if ans >= max_lim:
        print(max_lim)
        exit()
print(max(ans_li))
