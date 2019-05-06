group_A = [1,3,5,7,8,10,12]
group_B = [4,6,9,11]
group_C = [2]
x,y = map(int,input().split())
if(x in group_A):
    if(y in group_A):
        print("Yes")
    else:
        print("No")
elif(x in group_B):
    if(y in group_B):
        print("Yes")
    else:
        print("No")
else:
    if(y in group_C):
        print("Yes")
    else:
        print("No")