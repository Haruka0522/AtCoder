X = input()
Flag = True
while Flag:
    Flag = False
    sue = X[-1]
    if X[-2:] == "ch":
        X = X[:-2]
        Flag = True
    elif sue == "o":
        X = X[:-1]
        Flag = True
    elif sue == "k":
        X = X[:-1]
        Flag = True
    elif sue == "u":
        X = X[:-1]
        Flag = True
    if len(X) <= 1:
        break
if X == "":
    print("YES")
else:
    print("NO")
