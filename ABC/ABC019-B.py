S = input()
ans = ""
cnt = 1
for i in range(len(S)-1):
    if S[i] == S[i+1]:
        cnt += 1
    else:
        ans += S[i] + str(cnt)
        cnt = 1
ans += S[-1] + str(cnt)
print(ans)
