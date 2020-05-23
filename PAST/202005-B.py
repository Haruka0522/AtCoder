from collections import defaultdict
N,M,Q = map(int,input().split())
scores = [N]*M
solved = defaultdict(list)
ans = []
for i in range(Q):
    s = list(map(int,input().split()))
    if s[0] == 2:
        n,m = s[1] - 1,s[2] - 1
        scores[m] -= 1
        solved[n].append(m)
    else:
        n = s[1] - 1
        ans_tmp = 0
        for i in solved[n]:
            ans_tmp += scores[i]
        ans.append(ans_tmp)
for i in ans:
    print(i)
