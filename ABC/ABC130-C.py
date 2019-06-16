W,H,x,y = map(int,input().split())
if W/2 == float(x) and H/2 == float(y):
    print(W*H/2,1)
else:
    print(W*H/2,0)
