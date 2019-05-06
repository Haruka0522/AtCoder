x,y = input().split()
if(int(x,16)<int(y,16)):
    print("<")
elif(x==y):
    print("=")
else:
    print(">")