A = int(input())
B = int(input())
C = int(input())
ABC = [A,B,C]
if(min(ABC)==A):
    print(3)
    if(max(ABC)==B):
        print(1)
        print(2)
    else:
        print(2)
        print(1)
elif(max(ABC)==A):
    print(1)
    if(min(ABC)==B):
        print(3)
        print(2)
    else:
        print(2)
        print(3)
else:
    print(2)
    if(min(ABC)==B):
        print(3)
        print(1)
    else:
        print(1)
        print(3)    