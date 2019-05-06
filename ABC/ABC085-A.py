flag = 0
a = input().split("/")
del a[0]
a = ["2018",] + a
for i in a:
    flag += 1
    if(flag == 3):
        print(i)
    else:
        print(i,end="/")