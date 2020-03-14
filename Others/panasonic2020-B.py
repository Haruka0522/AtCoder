H,W = map(int,input().split())
if H == 1 or W == 1:
    print(1)
    exit()
a = -(-H//2)
b = -(-W//2)
c = H//2
d = W//2
print(a*b+c*d)
