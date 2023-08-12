n = int(input())
s = input()

a = False
b = False
c = False
for i, s_i in enumerate(list(s)):
    if s_i == "A":
        a = True
    if s_i == "B":
        b = True
    if s_i == "C":
        c = True
    if a and b and c:
        print(i+1)
        break
