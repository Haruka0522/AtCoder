x,a,b = map(int,input().split())
if(-a+b > x):
    print("dangerous")
elif(-a+b > 0):
    print("safe")
else:
    print("delicious")