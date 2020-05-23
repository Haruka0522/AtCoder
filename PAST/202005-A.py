s = input()
t = input()
if s == t:
    print("same")
else:
    s = s.upper()
    t = t.upper()
    if s == t:
        print("case-insensitive")
    else:
        print("different")
