l,x = map(int,input().split())
if x//l % 2 == 1:
    print(l-(x%l))
else:
    print(x%l)
