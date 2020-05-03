from itertools import combinations_with_replacement
N,M,Q = map(int,input().split())
ans_li = []
abcd = [tuple(map(int,input().split())) for _ in range(Q)]
for A in combinations_with_replacement(range(1,M+1),N):
    ans = 0
    for a,b,c,d in abcd:
        if A[b-1] - A[a-1] == c:
            ans += d
    ans_li.append(ans)
print(max(ans_li))
