S,L,R = map(int,input().split())
if L <= S <= R:
    print(S)
elif abs(L-S) > abs(R-S):
    print(R)
else:
    print(L)
