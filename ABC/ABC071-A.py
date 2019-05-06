x,a,b = map(int,input().split())
A_X = abs(a-x)
B_X = abs(b-x)
if(A_X > B_X):
    print("B")
else:
    print("A")