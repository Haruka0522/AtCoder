N = int(input())
S = list(input())
ans_tmp = 0
for i in S:
    if i == "A":
        ans_tmp += 4
    elif i == "B":
        ans_tmp += 3
    elif i == "C":
        ans_tmp += 2
    elif i == "D":
        ans_tmp += 1
print(ans_tmp/N)
