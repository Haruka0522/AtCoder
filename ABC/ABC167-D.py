N,K = map(int,input().split())
A_li = list(map(int,input().split()))
junban = [1,]
idx = 0
flag = False
flag2 = False
check = [0]*N
while True:
    tmp = A_li[idx]
    if check[idx]:
        if flag:
            flag = True
        else:
            flag2 = True
    junban.append(tmp)
    check[idx] = 1
    idx = tmp - 1
    if flag2:
        break
#print(junban)
syuuki = []
check = [0]*N
for i in junban[::-1]:
    syuuki.append(i)
    if check[i-1]:
        break
    check[i-1] = 1
syuuki = syuuki[::-1][:-1]
#print(syuuki)
saisyo = 0
a = len(syuuki)
for i in range(len(junban)):
    if junban[i:i+a] == syuuki:
        saisyo = i
        break
#print(saisyo)
indekkusu = (K-saisyo)%len(syuuki)
print(syuuki[indekkusu])
