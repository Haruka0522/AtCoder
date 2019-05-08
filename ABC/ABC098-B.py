N = int(input())
S = input()
ans_list = []
abc_list = [chr(i) for i in range(97,97+26)]
for i in range(1,N):
    ans = 0
    S1 = list(S[:i])
    S2 = list(S[i:])
    for j in abc_list:
        if(j in S1 and j in S2):
            ans += 1
    ans_list.append(ans)
print(max(ans_list))
