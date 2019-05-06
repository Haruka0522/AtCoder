# WA回答
import copy
N = int(input())
S = list(input())
S_2 = copy.copy(S)
ans = 0
ans_2 = 0

for i in range(N-1):
    if (S[i] == "#" and S[i + 1] == "."):
        S[i + 1] = "#"
        ans += 1

for j in range(N-1):
    if (S_2[j] == "#" and S_2[j + 1] == "."):
        S_2[j] = "."
        ans_2 += 1

print(min(ans, ans_2))
