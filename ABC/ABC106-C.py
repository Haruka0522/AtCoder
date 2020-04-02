S = list(input())
K = int(input())
for i in S:
    if i != "1":
        break
i = S.index(i)
if K <= i:
    print(1)
else:
    print(S[i])
