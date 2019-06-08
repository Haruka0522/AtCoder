S = input()
if "C" in S and "F" in S:
    if S.index("C") < len(S) - S[::-1].index("F"):
        print("Yes")
        exit()
print("No")
