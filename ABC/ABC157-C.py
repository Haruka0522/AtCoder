N,M = map(int,input().split())
values = []
for i in range(N):
    values.append([])
for i in range(M):
    s,c = map(int,input().split())
    values[s-1].append(c)

#同じ桁に2つ以上候補があるなら-1
for i in values:
    if len(set(i)) >= 2:
        print(-1)
        exit()

#最上位桁に候補がないときは1を補う
if values[0] == list():
    if N != 1:
        values[0].append(1)

#候補がない桁は0を補う
for i in range(N):
    if len(values[i]) == 0:
        values[i].append(0)

#探索
for i in range(1000):
    i = [int(j) for j in list(str(i))]
    if len(i) != N:
        continue
    if N==3:
        if i[0] in values[0] and i[1] in values[1] and i[2] in values[2]:
            print("".join([str(j) for j in i]))
            exit()
    elif N==2:
        if i[0] in values[0] and i[1] in values[1]:
            print("".join([str(j) for j in i]))
            exit()
    else:
        if i[0] in values[0]:
            print("".join([str(j) for j in i]))
            exit()
print(-1)

