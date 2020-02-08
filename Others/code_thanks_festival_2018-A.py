T,A,B,C,D = map(int,input().split())
if T >= A + C:
    print(B + D)
elif T >= C:
    print(D)
elif T >= A:
    print(B)
else:
    print(0)
