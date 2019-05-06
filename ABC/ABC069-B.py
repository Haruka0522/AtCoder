S = list(input())
saisho = S[0]
del S[0]
saigo = S[-1]
del S[-1]
kazu = str(len(S))
print(saisho+kazu+saigo)
