import numpy as np
H,W = map(int,input().split())
table = []
for i in range(H):
    col = list(input())
    table.append(col)
table = np.array(table)
for i in range(1,H):
    for j in range(1,W):
        bubun = table[i-1:i+2,j-1:j+2]
        if bubun.shape != (3,3):
            continue
        center = bubun[1,1]
        if center == "#" and bubun[0,1] == "." and bubun[1,0] == "." and bubun[1,2] == "." and bubun[2,1] == "." :
            print("No")
            exit()
        #print(bubun)
print("Yes")
