N = int(input())
S = list(input())
ans = 0
for i in range(N-2):
    if S[i:i+3] == ["A","B","C"]:
        ans += 1
print(ans)
