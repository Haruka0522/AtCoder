s = set(list(input()))
t = set(list(input()))

group1 = [set(["A", "B"]), set(["B", "C"]), set(["C", "D"]), set(["D", "E"]), set(["E", "A"])]
group2 = [set(["A", "C"]), set(["B", "D"]), set(["C", "E"]), set(["D", "A"]), set(["E", "B"])]

if s in group1 and t in group1:
    print("Yes")
elif s in group2 and t in group2:
    print("Yes")
else:
    print("No")
