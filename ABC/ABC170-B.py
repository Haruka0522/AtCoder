X,Y = map(int,input().split())
for turu in range(1000):
    for kame in range(1000):
        if turu+kame == X and 2*turu+4*kame == Y:
            print("Yes")
            exit()
print("No")
