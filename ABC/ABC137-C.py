N = int(input())
detayatsu = dict()
ans = 0
for i in range(N):
    S_i = "".join(sorted(list(input())))
    if S_i in detayatsu.keys():
        ans += detayatsu[S_i]
        detayatsu[S_i] += 1
    else:
        detayatsu[S_i] = 1
print(ans)
