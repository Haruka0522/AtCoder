import numpy as np
H,W = map(int,input().split())
table = [["."]*(W+2),]
for _ in range(H):
    table.append([".",]+list(input())+[".",])
table.append(["."]*(W+2))
table = np.array(table)
ans = []
#print(table)
for h in range(H):
    for w in range(W):
        mawari = table[h:h+3,w:w+3]
        #print(mawari)
        if mawari[1,1] == ".":
            ans.append(np.count_nonzero(mawari=="#"))
        else:
            ans.append("#")
ans = np.array(ans).reshape(H,W).astype(np.unicode)
for i in ans:
    print("".join(i))
