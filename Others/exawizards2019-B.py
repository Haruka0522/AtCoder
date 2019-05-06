N = int(input())
S = list(input())
R_count = 0
B_count = 0
for i in S:
    if(i == "R"):
        R_count += 1
    else:
        B_count += 1
if(R_count > B_count):
    print("Yes")
else:
    print("No")
