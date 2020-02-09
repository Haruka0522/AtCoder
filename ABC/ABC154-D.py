N,K = map(int,input().split())
p_list = list(map(int,input().split()))
ans_list = []
def E(me):
    if me == 1:
        return 1
    else:
        return ((1+me)*me/2)/me
E_list_ruisekiwa = [0,]
for i in range(N):
    E_list_ruisekiwa.append(E_list_ruisekiwa[i]+E(p_list[i]))

ans = 0
for i in range(N-K+1):
    ans = max(E_list_ruisekiwa[i+K]-E_list_ruisekiwa[i],ans)
print(ans)
