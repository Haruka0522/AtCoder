A = int(input())
seki_li = [1,]
for i in range(1,int(A/2)+1):
    seki_li.append(i*(A-i))
print(max(seki_li))