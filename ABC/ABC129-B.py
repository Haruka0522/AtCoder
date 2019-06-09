N = int(input())
W = list(map(int,input().split()))
ans = []
for T in range(1,N):
    S1 = W[:T]
    S2 = W[T:]
    #print(S1,S2)
    ans.append(abs(sum(S1)-sum(S2)))
print(min(ans))
