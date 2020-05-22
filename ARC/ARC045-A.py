S = input().split()
ans = []
for i in S:
    if i == "Left":
        ans.append("<")
    elif i == "Right":
        ans.append(">")
    else:
        ans.append("A")
print(" ".join(ans))

