S = input()
kami = int(S[:2])
simo = int(S[2:])
if(1 <= kami and kami<=12 and 1 <= simo and simo<=12):
    print("AMBIGUOUS")
elif(1<=kami and kami<=12):
    print("MMYY")
elif(1<=simo and simo<=12):
    print("YYMM")
else:
    print("NA")

