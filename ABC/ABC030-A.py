a,b,c,d = map(int,input().split())
takahashi = b/a
aoki = d/c
if(takahashi == aoki):
    print("DRAW")
elif(takahashi < aoki):
    print("AOKI")
else:
    print("TAKAHASHI")