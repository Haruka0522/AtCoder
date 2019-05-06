S = list(map(int,input()))
ketasu = len(S)
sa_list = []
for i in range(ketasu-2):
    toridashita_kazu = 100*S[i]+10*S[i+1]+S[i+2]
    sa = abs(toridashita_kazu - 753)
    sa_list.append(sa)
print(min(sa_list))