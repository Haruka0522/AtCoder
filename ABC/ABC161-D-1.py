K = int(input())
i = 1
while True:
    a = list(str(i))
    flag = True
    for j in range(len(a)-1):
        if abs(int(a[j])-int(a[j+1])) > 1:
            flag = False
            break
    if flag:
        print(i)
    i += 1




