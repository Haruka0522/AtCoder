S = list(input())
S_syusei = []
S_syusei.append(S[0].upper())
del S[0]
for i in S:
    S_syusei.append(i.lower())
print("".join(S_syusei))