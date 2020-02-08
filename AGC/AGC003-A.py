S = sorted(set(list(input())))
if S == ["E","N","S","W"]:
    print("Yes")
elif S == ["E","W"]:
    print("Yes")
elif S == ["N","S"]:
    print("Yes")
else:
    print("No")
