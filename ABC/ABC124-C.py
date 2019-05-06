S = list(input())
flag = 0
ans_1 = 0
ans_2 = 0
# 最初を変える
S1 = S[0]
if (S1 == "0"):
    flag_a = 1
else:
    flag_a = 0
for i in range(1, len(S)):
    if (flag_a == 0):
        if (S[i] == "1"):
            ans_1 += 1
        flag_a = 1
    else:
        if (S[i] == "0"):
            ans_1 += 1
        flag_a = 0
if (len(S) != 1):
    if (S[0] != S[1]):
        ans_1 = 1000000

# 最初を変えない
S1 = S[0]
if (S1 == "1"):
    flag_b = 1
else:
    flag_b = 0
for i in range(1, len(S)):
    if (flag_b == 0):
        if (S[i] == "0"):
            ans_2 += 1
        flag_b = 1
    else:
        if (S[i] == "1"):
            ans_2 += 1
        flag_b = 0
if (len(S) != 1):
    if (S[0] == S[1]):
        ans_2 = 1000000

print(min(ans_1, ans_2))
