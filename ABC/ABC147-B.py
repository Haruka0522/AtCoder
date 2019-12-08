S = list(input())
S_rev = [i for i in S[::-1]]
ans = 0
for i in range(len(S)):
    if S[i] != S_rev[i]:
        ans += 1
print(ans//2)

