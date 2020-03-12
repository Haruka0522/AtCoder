S = list(input())
original = len(S)
flag = True
while flag:
    flag = False
    i = 0
    while i+1 < len(S):
        if S[i] != S[i+1]:
            flag = True
            del S[i:i+2]
        i += 1
print(original-len(S))
