A,B,C = input().split()
if (A==B and B!=C) or (B==C and C!=A) or (C==A and A!= B):
    print("Yes")
else:
    print("No")
