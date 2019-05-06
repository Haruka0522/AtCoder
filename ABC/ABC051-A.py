a = input().split(",")
n = 0
for i in a:
    n += 1
    if(n<3):
        print(i,end=" ")
    else:
        print(i)
