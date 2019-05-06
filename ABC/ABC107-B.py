H,W = map(int,input().split())
S = []
m = []
for i in range(H):
    S.append(list(input()))

for i in S:
    if(i.count(".")==len(i)):
        S.remove(i)

for i in range(W):
    m = []
    for j in S:
        m.append(j[i])
    if(m.count(".")==len(m)):
        for k in S:
            del k[i]

print(S)
