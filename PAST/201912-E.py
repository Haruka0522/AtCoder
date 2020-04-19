N,Q = map(int,input().split())
table = [([],[]) for i in range(N)] # [([follow],[follower])]
for i in range(Q):
    S = input().split()
    if S[0] == "1":
        a,b = int(S[1])-1,int(S[2])-1
        table[a][0].append(b)
        table[b][1].append(a)
    elif S[0] == "2":
        a = int(S[1])-1
        for j in table[a][1]:
            table[a][0].append(j)
            table[j][1].append(a)
    elif S[0] == "3":
        a = int(S[1])-1
        tmp = table[a][0].copy()
        for x in tmp:
            for j in table[x][0]:
                if j == a:
                    continue
                else:
                    table[a][0].append(j)
                    table[j][1].append(a)

for follow,follower in table:
    result = ["N"]*N
    for i in follow:
        result[i] = "Y"
    print("".join(result))
