a,b = map(int,input().split())
A = (a+1)*b
B = (b+1)*a
if(A<B):
    print(B)
else:
    print(A)