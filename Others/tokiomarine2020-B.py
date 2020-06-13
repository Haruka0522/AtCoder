A,V = map(int,input().split())
B,W = map(int,input().split())
T = int(input())
v = V - W
sa = abs(A-B)
if v <= 0:
    print("NO")
else:
    if sa / v <= T:
        print("YES")
    else:
        print("NO")
