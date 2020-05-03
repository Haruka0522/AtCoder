S = input()
S_spl = S.split("+")
ans = 0
for i in S_spl:
    if "0" in list(i):
        continue
    for j in list(str(i)):
        if j != "0" and j != "*":
            ans += 1
            break
print(ans)
