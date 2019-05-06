A,B,C,K = map(int,input().split())
S,T = map(int,input().split())
waribikimae = A*S + B*T
if(S+T>=K):
    goukei = waribikimae - C*(S+T)
    print(goukei)
else:
    print(waribikimae)