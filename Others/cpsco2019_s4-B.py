n,d = map(int,input().split())
S = [input() for i in range(d)]
ans = []
for i in range(d):
    for j in range(d):
        count = 0
        A = list(S[i])
        B = list(S[j])
        for k in range(n):
            if A[k]=="o" or B[k]=="o":
                count += 1
        ans.append(count)
print(max(ans))
