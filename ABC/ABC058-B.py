l1 = list(input())
l2 = list(input())
ans = []
for i in range(len(l1)):
    try:
        ans.append(l1[i])
        ans.append(l2[i])
    except:
        a = 0
print("".join(ans))