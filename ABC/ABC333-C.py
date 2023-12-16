n = int(input())


keta = 12
rep = ["1"*i for i in range(1, keta+1)]
target = set([])
for i in range(keta):
    for j in range(keta):
        for k in range(keta):
            target.add(int(rep[i]) + int(rep[j]) + int(rep[k]))
target = sorted(list(target))
print(sorted(target)[n-1])
