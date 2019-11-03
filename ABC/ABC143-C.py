N = int(input())
S = list(input())
convert = [S[0]]
for i in range(N-1):
    if S[i] != S[i+1]:
        convert.append(S[i+1])
print(len(convert))
