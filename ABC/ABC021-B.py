N = int(input())
a,b = map(int,input().split())
K = int(input())
P_li = list(map(int,input().split()))
if a in P_li or b in P_li or len(set(P_li)) != len(P_li):
    print("NO")
else:
    print("YES")
